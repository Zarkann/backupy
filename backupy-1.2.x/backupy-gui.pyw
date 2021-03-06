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
from Tkinter import *
import backupy_strings
import datetime
import errno
import os
import shutil
import tarfile

# ~Code~
root = Tk()
root.title("backupy - a backup utility tool")

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
        self.root_dir = Entry(self.menu)
        self.root_dir.grid(row = 1, column = 2)
        self.root_dir.focus_force()

        # Second entry-bar with label.
        self.dst_label = Label(self.menu, text = "Destination")
        self.dst_label.grid(row = 2, column = 1)
        self.dst_dir = Entry(self.menu)
        self.dst_dir.grid(row = 2, column = 2)

        # Check-button asking if you want to archive the backup.
        self.archive_ans = BooleanVar()
        self.archive_btn = Checkbutton(self.menu, text = "Archive.", \
        variable = self.archive_ans, onvalue = True, offvalue = None)
        self.archive_btn.grid(row = 3, column = 1)

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
        # Checks if the program was given any entries.
        if self.root_dir.get() != '' or self.dst_dir.get() != '':
            # Raises an error message should src_dir not exist.
            if not os.path.exists(self.root_dir.get()):
                self.no_root_dir()

            # Adds dst_dir should it not exist in the file system.
            elif not os.path.exists(self.dst_dir.get()):
                try:
                    os.makedirs(self.dst_dir.get())
                except OSError as self.e:
                    self.error_window()

            # NOTICE! I break the previous if-loop here to make sure that when
            # dst_path does not exist the program will check again if dst_path
            # exists. Now it hopefully does and thus goes on to copying the
            # files.
            if os.path.exists(self.dst_dir.get()):
                # Creates a folder named backup-<YYYYMMDD>-<hhmm>
                self.new_baup_time = \
                datetime.datetime.now().strftime("%Y%m%d-%H%M")
                self.folder_name = "backup-" + self.new_baup_time
                if os.name == "posix":
                    self.folder_path = self.dst_dir.get() + "/" + \
                    self.folder_name
                elif os.name == "nt":
                    self.folder_path = self.dst_dir.get() + "\\" + \
                    self.folder_name

                # LET THERE BE COPIES!
                # This is the copy function of the script.
                try:
                    shutil.copytree(self.root_dir.get(), self.folder_path)
                except OSError as self.e:
                    self.error_window()
                    pass

            # Creates a pop-up saying if the job is completed.
            # Add functionality to say if the job was completed succesfully
            # or if it failed later.
            if (not self.archive_ans.get() == True) and (os.path.isdir(\
            self.folder_path) == True):
                self.completed_job()
            elif self.archive_ans.get() == True:
                self.archive_ck()
            else:
                self.awry_job()
                

    # If the backup is supposed to be archived, this will perform the
    # archivation process.
    def archive_ck(self): 
        # Attempt to create the tarfile folder_path + tar.gz
        try:
            self.arc_file = tarfile.open(self.folder_path + ".tar.gz", \
            "w:gz")
            self.arc_file.add(self.folder_path)
            self.arc_file.close()
        except tarfile.CompressionError as e:
            self.awry_job()
        except tarfile.TarError as e:
            self.awry_job()
        # Check if folder_path exists, if so, remove folder_path
        try:
            if os.path.isdir(self.folder_path):
                shutil.rmtree(self.folder_path)
        except shutil.Error as e:
            self.awry_job()

        if os.path.isfile(self.folder_path + ".tar.gz") == True:
            self.completed_job()
        else:
            self.awry_job()

    # Exit-button function
    def exitclick(self):
        self.main_parent.destroy()

    # Help-button function
    def helpclick(self):
        # Creates a pop-up named help_pop
        self.help_pop = Toplevel()
        self.help_pop.title("Help")

        # The main message of the pop-up
        self.help_text = """
        This is backupy.
        
        To use backupy simply enter the source directory
        into the entry bar named source.
        You also have to specify a destination directory
        into the entry bar named destination.
        After this simply decide if you want to archive
        the folders by pressing the archive checkbutton.
        then press backup to start the backup job.
        
        Thank you for using backupy
        """
        self.help_msg = Message(self.help_pop, text = self.help_text)
        self.help_msg.grid(row = 1, column = 1)

        # Cancel button to close the pop-up
        self.cancel_button = Button(self.help_pop,\
        command = self.help_pop.destroy)
        self.cancel_button.configure(text = "Cancel", background = "grey")
        self.cancel_button.grid(row = 2, column = 1)

    # License-button function
    def licenseclick(self):
        # Creates a pop-up named license_pop
        self.license_pop = Toplevel()
        self.license_pop.title("License")

        # The main message of the pop-up
        self.license_text = """
        This program is licensed under the GPLv3
        which should've been supplied with this 
        program.
        
        Check the programs root directory or go
        to http://www.gnu.org/licenses/
        """
        self.license_msg = Message(self.license_pop, text = self.license_text)
        self.license_msg.grid(row = 1, column = 1)

        # Cancel button to close the pop-up
        self.cancel_button = Button(self.license_pop,\
        command = self.license_pop.destroy)
        self.cancel_button.configure(text = "Cancel", background = "grey")
        self.cancel_button.grid(row = 2, column = 1)

    # Error pop-up
    def error_window(self):
        # Creates the pop-up window
        self.error_pop = Toplevel()
        self.error_pop.title("Error")

        # What is supposed to be written in the error message?
        self.error_msg = Message(self.error_pop, text = self.e)
        self.error_msg.grid(row = 1, column = 1)

        # Dismiss-button
        self.error_dis = Button(self.error_pop,\
        command = self.error_pop.destroy)
        self.error_dis.configure(text = "Dismiss", background = "grey")
        self.error_dis.grid(row = 2, column = 1)

    def no_root_dir(self):
        # Pops up if the user didn't enter a source root.
        self.no_root = Toplevel()
        self.no_root.title("WRONG!")

        # The message itself
        self.no_root_msg = Message(self.no_root, text = """
        You forgot to enter a source root!
        For a backup to be made you have to enter
        something to be backed  up!
        """)
        self.no_root_msg.grid(row = 1, column = 1)

        # The escape button
        self.no_root_dis = Button(self.no_root, command = self.no_root.destroy)
        self.no_root_dis.configure(text = "Dismiss", background = "grey")
        self.no_root_dis.grid(row = 2, column = 1)

    def completed_job(self):
        self.done_pop = Toplevel()
        self.done_pop.title("Job complete!")
        self.done_txt = """
        The job has been completed!
        Thanks for using backupy.
        """
        self.done_msg = Message(self.done_pop, text = self.done_txt)
        self.done_msg.grid(row = 1, column = 1)

        # Escape button
        self.done_exit = Button(self.done_pop, \
        command = self.main_parent.destroy)
        self.done_exit.configure(text = "Exit", background = "grey")
        self.done_exit.grid(row = 2, column = 1)

    def awry_job(self):
        self.awry_pop = Toplevel()
        self.awry_pop.title("Something went awry")
        self.awry_txt = """
        Something went awry. Try again.
        """
        self.awry_msg = Message(self.awry_pop, text = self.awry_txt)
        self.awry_msg.grid(row = 1, column = 1)
        self.awry_exit = Button(self.awry_pop,\
        command = self.main_parent.destroy)
        self.awry_exit.configure(text = "Exit", background = "grey")
        self.awry_exit.grid(row = 2, column = 1)

root_instance = main(root)
root.mainloop()