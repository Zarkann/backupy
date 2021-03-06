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
    print(backupy_strings.install_intro)

    # Creates the directory /usr/local/bin/backupy for backupy to reside in.
    try:
        print("\tCreating /usr/local/bin/backupy...")
        os.mkdir("/usr/local/bin/backupy")
        print("\tDONE!")
    except OSError as error:
        print(error)
        pass

    # For-loop that checks what files is in the backupy directory.
    backupy_files = []
    for loc_root, loc_sub, loc_file in os.walk("./"):
        backupy_files.append(loc_file)
    
    # For-loop that copies the files from the directory where the installer is
    # to /usr/local/bin where backupy will reside, ensuring that backupy is
    # reachable from whatever user is logged in to the machine.
    for entry in backupy_files[0]:
        try:
            print("\tCopying %r to /usr/local/bin/backupy") % entry
            shutil.copy2("./" + entry, "/usr/local/bin/backupy")
            print("\tDONE!")
        except shutil.Error as error:
            print(error)
            continue

    # Finds out what home directories exist in the os.
    home_user = []
    try:
        for home_root, home_dir, home_files in os.walk("/home"):
            home_user.append(home_dir)
    except OSError as error:
        print(error)
        sys.exit(2)

    # Adds the alias backupy in ~/.bashrc of all users.
    for entry in home_user[0]:
        # Attempts to change directory. Will print an error statement if it fails.
        try:
            os.chdir("/home/" + entry)
        except OSError as error:
            print(error)
            continue
        # Attempts to open the file .bashrc. If it fails it will print an error.
        try:
            bashrc_file = open(".bashrc", "a")
            print("\tAppends alias to the ~/.bashrc file of %r") % entry
            bashrc_file.write("\n\n# backupy alias\n")
            bashrc_file.write("alias backupy='python /usr/local/bin/backupy/backupy.py'")
            bashrc_file.close()
            print("\tDONE!")
        except IOError as error:
            print(error)
            continue
    # Edits the .bashrc file for the root user.
    os.chdir("/root")
    try:
        bashrc_file = open(".bashrc", "a")
        print("\tAppends alias to the ~/.bashrc file of the root user.")
        bashrc_file.write("\n\n# backupy alias\n")
        bashrc_file.write("alias backupy='python /usr/local/bin/backupy/backupy.py'")
        bashrc_file.close()
        print("\tDONE!")
    except IOError as error:
        print(error)
        print("\tSomething went wrong. You have to add the alias yourself.")
        pass
    print("\tAliases added.")
    print("\n")
    print("\tThank you for installing backupy on your system.")
    print("\tPlease log out and log in again to make the aliases work.")
    print("\tHave a nice day.")

def install_nt():
    print(backupy_strings.not_supported)

installer()
exit()