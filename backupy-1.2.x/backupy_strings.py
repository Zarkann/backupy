#!/usr/bin/env python

# Backup script for the course Linux Scripting, Nackademin LS11
# This file contains strings for use in the main script.
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

__VERSION__ = "1.2.1"

__AUTHOR__ = "Jimmie Odelius"

help_text = (
"    backup.py is a script to be used for backing up your chosen directories.\n"
"    You can do this with the following syntax.\n\n"
"    backup.py -s <source directory> -d <destination directory>\n"
"    If you also want to compress your backup folder into a\n"
"    .tar archive. Enter the flag '-a'\n"
"    If you want to 'install' the script to be called from\n"
"    the command prompt. Run the command -i.\n\n"
"    backup.py should work with both python 2.x and 3.x\n")

not_supported = ("    Your operating system is not supported.\n"
"    Please wait for an update or add support yourself.\n"
"    Have a nice day.\n")

easter = ("    This is an easter egg.\n"
"    It is not particularly tasty.\n")

install_intro = (
"    backupy will now be installed as a callable command on the command\n"
"    prompt. You may of course do so manually if you wish.\n"
"    Make sure that you have permission to edit the files of the other\n"
"    users of the system. (Including '/root/.bashrc')\n")