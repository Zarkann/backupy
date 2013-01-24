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
# Meta-data variables
__AUTHOR__ = "Jimmie Odelius"
__VERSION__ = "0.1.2"

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
        os.makedirs("/usr/local/bin/backupy")
        shutil.copytree(".", "/usr/local/bin/backupy")
    elif os.path.exists("/usr/local/bin/backupy"):
        shutil.copytree("/usr/local/bin/backupy")

    # Finds out what home directories exist in the os.
    home_user = []
    for home_root, home_dir, home_files in os.walk("/home"):
        home_user.append(home_dir)
    # Removes all sub-lists except the first one containing the home directories.
    home_user = home_user[0]
    # Adds the alias backupy in ~/.bashrc of all users.
    for entry in home_user:
        print("Function to search and replace an alias in .bashrc")
    print("Functino to search and replace an alias in /root/.bashrc")

def install_nt():
    print("Your operating is not yet supported.")
    print("You can either wait for an update or take matters into your own hands.")
    print("Whatever you choose. Have a nice day. :)")

installer()
exit()