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
import datetime
import getopt
import gzip
import os
import shutil
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
        opts, args = getopt.getopt(argv,"aheis:d:",["root_dir=","dst_dir="])
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
            print("\n\nbackup.py should work with both python 2.x and 3.x")
            exit()
        elif opt in ("-s"):
            root_dir = arg
        elif opt in ("-d"):
            dst_dir = arg
        elif opt in ("-i"):
            print("This will install the script to your OS.")
            print("Support for this is not available in this version.")
            print("Please use SETUP.py manually.")
        elif opt in ("-e"):
            print("This is an easteregg.")
            print("It's not particularly yummy.")
        elif opt in ("-a"):
            print("Your directory will be archived.")
            archive = True

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

        # If the dst_dir exists. Do this.
        elif os.path.exists(dst_dir):
            # Self-explanatory. Prints the chosen source and destination
            # directories.
            print("Given source directory tree", root_dir)
            print("Given destination directory tree", dst_dir)

            # Creates a folder named backup-<YYYYMMDD>-<hhmm>.
            new_baup_time = datetime.datetime.now().strftime("%Y%m%d-%H%M")
            folder_name = "backup-" + new_baup_time
            folder_path = dst_dir + "\\backup-" + new_baup_time

            # This is the main copy function of the script. Which will copy
            # everything from the src_root
            shutil.copytree(root_dir, folder_path, symlinks=False, ignore=None)
            print("DONE!")

            # If the -a flag was entered backupy will commence its archive
            # if-loop. Archiving the backup<YYYYMMDD-hhmm> folder.
            if archive == True:
                print("Creating .tar-archive...")
                arc_file = tarfile.open(folder_path + ".tar", "w")
                arc_file.add(folder_path)
                new_folder_path = folder_path + ".tar"
                arc_file.close()
                print("DONE!")
                print("Compressing ", new_folder_path, "....")
                com_arc_file = gzip.open(new_folder_path + ".gz", "wb")
                com_arc_file.write(folder_path)
                com_arc_file.close()
                print("DONE!")
    sys.exit()
    
# Runs the functionp
if __name__ == "__main__":
    main(sys.argv[1:])