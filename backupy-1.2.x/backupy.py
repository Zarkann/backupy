#!/usr/bin/env python

# Backup script for the course Linux Scripting, Nackademin LS11
# Copyright (C) 2013  Jimmie Odelius
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# ~Modules~
# Imports the modules the script will use.
import backupy_strings
import datetime
import errno
import getopt
import os
import shutil
import subprocess
import sys
import tarfile

# ~Functions~
# The functions making up the script
def main(argv):
    # Creates the empty variables needed in the script
    root_dir = ''
    dst_dir = ''
    archive = False
    
    # Looks for arguments if any.
    try:
        opts, args = getopt.getopt(argv,"aheivms:d:")
    # Specifies what happens if a there is no viable commands.
    except getopt.GetoptError:
        print("\tCommand not found. Use the -h for help.")
        sys.exit(2)

    # Defines the commands usable with the script.
    for opt, arg in opts:
        if opt in ("-h"):
            print(backupy_strings.help_text)
        elif opt in ("-s"):
            root_dir = arg
        elif opt in ("-d"):
            dst_dir = arg
        elif opt in ("-i"):
            try:
                if os.name == "nt" or os.name == "posix":
                    subprocess.call([sys.executable, "SETUP.py"])
                    exit()
                else:
                    print(backupy_strings.not_supported)
            except OSError as error:
                print(error)
                sys.exit(2)
        elif opt in ("-e"):
            print(backupy_strings.easter)
        elif opt in ("-a"):
            print("\tYour directory will be archived.")
            archive = True
        elif opt in ("-v"):
            print("\tThis is backupy version %s.") % backupy_strings.__VERSION__
            print("\tCreated by %s.") % backupy_strings.__AUTHOR__

    # Makes sure the script is not without values on src_dir and dst_dir
    if root_dir != '' or dst_dir != '':
        # If the source path does not exist. End the script.
        if not os.path.exists(root_dir):
            print("\tSource path does not exist. Try again.")
            sys.exit(2)

        # Creates the destination tree if it does not exist.
        elif not os.path.exists(dst_dir):
            try:
                print("\tDestination path does not exist.")
                print("\tCreating destination directories")
                os.makedirs(dst_dir)
            except OSError as error:
                print(error)
                pass

        # NOTICE! I break the previous if-loop here to make sure that when
        # dst_path does not exist the program will check again if dst_path
        # exists. Now it hopefully does and thus goes on to copying the files.
        if os.path.exists(dst_dir):
            # Self-explanatory. Prints the chosen source and destination
            # directories.
            print("\tGiven source directory tree %r.") % root_dir
            print("\tGiven destination directory tree %r.") % dst_dir

            # Creates a folder named backup-<YYYYMMDD>-<hhmm>.
            new_baup_time = datetime.datetime.now().strftime("%Y%m%d-%H%M")
            folder_name = "backup-" + new_baup_time
            if os.name == "posix":
                folder_path = dst_dir + "/" + folder_name
            elif os.name == "nt":
                folder_path = dst_dir + "\\" + folder_name
 
            # This is the main copy function of the script. Which will copy
            # everything from the src_root
            try:
                print("\tCopying %r ...") % folder_path
                shutil.copytree(root_dir, folder_path)
                print("\tDONE!")
            # This error check still fails to function if a directory
            # already exists with the same name.
            except OSError as error:
                if error.errno == errno.EEXIST:
                    print(error)
                    print("The file already exists. Exiting program.")
                    sys.exit(2)

            # If the -a flag was entered backupy will commence its archive
            # if-loop. Archiving the backup<YYYYMMDD-hhmm> folder.
            if archive == True:
                print("\tCreating .tar-archive...")
                print("\tCompressing .tar-archive...")
                # Creates the file folder_path.tar.gz, a compressed tar archive.
                try:
                    arc_file = tarfile.open(folder_path + ".tar.gz", "w:gz")
                    # Adds folder_path to the tar.gz archive.
                    arc_file.add(folder_path)
                    # Writes the .tar.gz-file to disk.
                    arc_file.close()
                    print("\tDONE!")
                except tarfile.CompressionError as error:
                    print(error)
                    print("\tA compression error happened.")
                    print("\tExiting program.")
                    sys.exit(2)
                except tarfile.TarError as error:
                    print(error)
                    print("\tSomething went wrong with the tar operation.")
                    print("\tExiting program.")
                    sys.exit(2)
                try:
                    if os.path.isdir(folder_path):
                        print("\tRemoving unnecessary files...")
                        try:
                            shutil.rmtree(folder_path)
                            print("\tDONE!")
                        except shutil.Error as error:
                            print(error)
                            pass
                except OSError as error:
                    print(error)
                    pass
            print("\tBackup completed. Thanks for using backupy.")
            print("\tBye.")
    sys.exit()

# Runs the function
if __name__ == "__main__":
    main(sys.argv[1:])
    exit()