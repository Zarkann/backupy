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
import re
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
    # Copies backupy with meta-data to /usr/bin/local to make it "callable"
    # from the command prompt.
    if not os.path.exists("/usr/local/bin/backupy"):
        os.mkdir("/usr/local/bin/backupy [, mode=0557]")
    for root_dir, sub_dir, files in os.walk():
        print("Copying %r to /usr/local/bin/backupy ...") % files
        shutil.copy2(root_dir + sub_dir + files, "/usr/local/bin/backupy")
        print("DONE!")
    # Adds the alias backupy for users to make things tidier. Allowing users
    # to write backupy instead of backupy.py to use the program.
    print("Adding backupy as an alias...")
    # Creates the list home_dir
    home_dir = []
    # Contains a string with the file-name for the file containing aliases.
    file_name = "/.bashrc"
    # For loop to go through the users home-folders.
    print("Finding home folders.")
    for root_dir, sub_dir, files in os.walk("/home"):
        # If a path exists, for example /home/student, append path to home_dir.
        if os.path.isdir(root_dir + sub_dir):
            home_dir = ''.join(root_dir + sub_dir)
        # Creates the copy ~/.bashrc~ as a backup.
        shutil.copy2(home_dir + file_name, home_dir + file_name + "~")
        # Reads the file ~/.bashrc to alias_file.
        alias_file = open(home_dir + file_name).read()
        # Compiles the regex for use later.
        bashrc_regx = re.compile("(?<='# User specific aliases and functions\n')")
        regx_result = re.search(bashrc_regx, alias_file)

def install_nt():
    print("Your operating is not yet supported.")
    print("You can either wait for an update or take matters into your own hands.")
    print("Whatever you choose. Have a nice day. :)")

installer()
exit()