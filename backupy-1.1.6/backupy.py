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

# ~Meta~
# Meta-data variables.
__AUTHOR__ = "Jimmie Odelius"
__VERSION__ = "1.1.6c"

# ~Modules~
# Imports the modules the script will use.
import datetime
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
        print("Command not found. Use the -h for help.")
        sys.exit(2)

    # Defines the commands usable with the script.
    for opt, arg in opts:
        if opt in ("-h"):
            print("\nbackup.py is a script to be used for backing up your chosen directories.")
            print("You can do this with the following syntax.")
            print("backup.py -s <source directory> -d <destination directory>")
            print("If you also want to compress your backup folder into a")
            print(".tar archive. Enter the flag '-a'")
            print("\nIf you want to 'install' the script to be called from")
            print("the command prompt. Run the command -i.")
            print("\nbackup.py should work with both python 2.x and 3.x")
        elif opt in ("-s"):
            root_dir = arg
        elif opt in ("-d"):
            dst_dir = arg
        elif opt in ("-i"):
            if os.name == "nt" or os.name == "posix":
                subprocess.call([sys.executable, "SETUP.py"])
                exit()
            else:
                print("Your operating system is not supported.")
                print("Please wait for an update or add support yourself.")
                print("Have a nice day.")
        elif opt in ("-e"):
            print("This is an easteregg.")
            print("It's not particularly yummy.")
        elif opt in ("-a"):
            print("Your directory will be archived.")
            archive = True
        elif opt in ("-v"):
            print("This is backupy version %r.") % __VERSION__
            print("Created by %r.") % __AUTHOR__

    # Makes sure the script is not without values on src_dir and dst_dir
    if root_dir != '' or dst_dir != '':
        # If the source path does not exist. End the script.
        if not os.path.exists(root_dir):
            print("Source path does not exist. Try again.")
            sys.exit(2)

        # Creates the destination tree if it does not exist.
        elif not os.path.exists(dst_dir):
            print("Destination path does not exist.")
            print("Creating destination directories")
            os.makedirs(dst_dir)

        # NOTICE! I break the previous if-loop here to make sure that when
        # dst_path does not exist the program will check again if dst_path
        # exists. Now it hopefully does and thus goes on to copying the files.
        if os.path.exists(dst_dir):
            # Self-explanatory. Prints the chosen source and destination
            # directories.
            print("Given source directory tree %r.") % root_dir
            print("Given destination directory tree %r.") % dst_dir

            # Creates a folder named backup-<YYYYMMDD>-<hhmm>.
            new_baup_time = datetime.datetime.now().strftime("%Y%m%d-%H%M")
            folder_name = "backup-" + new_baup_time
            if os.name == "posix":
                folder_path = dst_dir + "/" + folder_name
            elif os.name == "nt":
                folder_path = dst_dir + "\\" + folder_name
 
            # This is the main copy function of the script. Which will copy
            # everything from the src_root
            shutil.copytree(root_dir, folder_path, symlinks=False, ignore=None)
            print("DONE!")

            # If the -a flag was entered backupy will commence its archive
            # if-loop. Archiving the backup<YYYYMMDD-hhmm> folder.
            if archive == True:
                print("Creating .tar-archive...")
                print("Compressing .tar-archive...")
                # Creates the file folder_path.tar.gz, a compressed tar archive.
                arc_file = tarfile.open(folder_path + ".tar.gz", "w:gz")
                # Adds folder_path to the tar.gz archive.
                arc_file.add(folder_path)
                # Writes the .tar.gz-file to disk.
                arc_file.close()
                print("DONE!")
                if os.path.isdir(folder_path):
                    print("Removing unnecessary files...")
                    shutil.rmtree(folder_path)
                    print("DONE!")
            print("Backup completed. Thanks for using backupy.")
            print("Bye.")
    sys.exit()

# Runs the function
if __name__ == "__main__":
    main(sys.argv[1:])
    exit()