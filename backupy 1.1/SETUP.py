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

# ~Functions~
# The functions making up the script
def install_script():
    if os.name == "nt":
        print("Your operating system is not supported in this version.")
        print("Support will be added in the foreseeable future.")
    elif os.name == "posix":
        print("Installation of the script now begins.")
        print("Copying backup.py to '/usr/local/bin'...")
        shutil.copy2("./backup.py", "/usr/local/bin")
        print("DONE!")
        print("Please note that you will have to create an alias as well as")
        print("setting executable permission on the script to make any user")
        print("use the script.")
    else:
        print("Your operating system is not supported in this version.")
        print("Either write your own install script or deal with it.")