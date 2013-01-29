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
import os
import shutil
import sys

# ~Functions~
# The functions making up the script
def installer():
    if os.name == "nt":
        install_nt()
    elif os.name == "posix":
        install_linux()

def install_linux():
    print("backupy will now be installed as a callable command on the command")
    print("prompt. You may of course do so manually if you wish.")
    print("Make sure that you have permission to edit the files of the other\n")
    print("users of the system. (Including '/root/.bashrc')")

    # Creates the directory /usr/local/bin/backupy for backupy to reside in.
    try:
        print("Creating /usr/local/bin/backupy...")
        os.mkdir("/usr/local/bin/backupy")
        print("DONE!")
    except OSError as error:
        print(error)
        pass

    # For-loop that checks what files is in the backupy directory.
    backupy_files = []
    for loc_root, loc_sub, loc_file in os.walk("./"):
        backupy_files.append(loc_file)
    
    for entry in backupy_files:
        try:
            print("Copying %r to /usr/local/bin/backupy") % loc_file
            shutil.copy2("./" + loc_file, "/usr/local/bin/backupy")
            print("DONE!")
        except shutil.Error as error:
            print(error)
            continue

    # Finds out what home directories exist in the os.
    home_user = []
    for home_root, home_dir, home_files in os.walk("/home"):
        home_user.append(home_dir)
    # Removes all sub-lists except the first one containing the home directories.
    home_user = home_user[0]

    # Adds the alias backupy in ~/.bashrc of all users.
    for entry in home_user:
        # Attempts to change directory. Will print an error statement if it fails.
        try:
            os.chdir("/home/" + entry)
        except OSError as error:
            print(error)
            continue
        # Attempts to open the file .bashrc. If it fails it will print an error.
        try:
            bashrc_file = open(".bashrc", "a")
            print("Appends alias to the ~/.bashrc file of %r") % entry
            bashrc_file.write("\n\n# backupy alias\n")
            bashrc_file.write("alias backupy='python /usr/local/bin/backupy/backupy.py'")
            bashrc_file.close()
            print("DONE!")
        except IOError as error:
            print(error)
            continue
    # Edits the .bashrc file for the root user.
    os.chdir("/root")
    bashrc_file = open(".bashrc", "a")
    print("Appends alias to the ~/.bashrc file of the root user.")
    bashrc_file.write("\n\n# backupy alias\n")
    bashrc_file.write("alias backupy='python /usr/local/bin/backupy/backupy.py'")
    bashrc_file.close()
    print("DONE!")
    print("Aliases added.")
    print("Thank you for installing backupy on your system.")
    print("Have a nice day.")

def install_nt():
    print("Your operating is not yet supported.")
    print("You can either wait for an update or take matters into your own hands.")

installer()
exit()