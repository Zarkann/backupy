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
__VERSION__ = "1.2.0"

# ~Modules~
# Imports the modules the script will use.
from Tkinter import *
import os

# ~Code~
root = Tk()
root.title("backupy - Back-up utility tool.")

class main:
    def __init__(self, parent):
        # Binds parent to the variable main_parent.
        self.main_parent = parent
        
        # Creates the root container.
        self.menu = Frame(parent)
        self.menu.grid()

        # First entry-bar with label.
        self.src_label = Label(self.menu, text = "Source")
        self.src_label.grid(row = 1, column = 1)
        self.src_dir = Entry(self.menu)
        self.src_dir.grid(row = 1, column = 2)
        self.src_dir.focus_force()

        # Second entry-bar with label.
        self.dst_label = Label(self.menu, text = "Destination")
        self.dst_label.grid(row = 2, column = 1)
        self.dst_dir = Entry(self.menu)
        self.dst_dir.grid(row = 2, column = 2)

        # Check-button asking if you want to archive the backup.
        self.archive_ck = Checkbutton(self.menu, text = "Archive.",
        onvalue = True, offvalue = None)
        self.archive_ck.grid(row = 3, column = 1)

        # Creates an ok-button
        self.ok_button = Button(self.menu, command = self.backupclick)
        self.ok_button.configure(text = "Backup", background = "grey")
        self.ok_button.grid(row = 4, column = 1)

        # Creates a cancel/exit-button
        self.exit_button = Button(self.menu, command = self.exitclick)
        self.exit_button.configure(text = "Cancel/Exit", background = "grey")
        self.exit_button.grid(row = 4, column = 2)
        
        # Creates a help-button
        self.help_button = Button(self.menu, command = self.helpclick)
        self.help_button.configure(text = "Help", background = "grey")
        self.help_button.grid(row = 4, column = 4)
        
        # Creates a license-button
        self.license_button = Button(self.menu, command = self.licenseclick)
        self.license_button.configure(text = "License", background = "grey")
        self.license_button.grid(row = 4, column = 5)

    # OK-button function
    def backupclick(self):
        print("Add backup-function here!")

    # Exit-button function
    def exitclick(self):
        self.main_parent.destroy()

    # Help-button function
    def helpclick(self):
        print("Add help-function here!")

    # License-button function
    def licenseclick(self):
        print("Add License-function here!")

root_instance = main(root)
root.mainloop()