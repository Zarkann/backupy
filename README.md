backupy
=======

This is my backup script I am currently writing in Python for a
course in my school primarily about bash but we are allowed to use
other languages as well.

Feel free to use and fork it if you want.

Usage
-----

The script works by taking several arguments. The syntax is.
    backupy.py [ ( -h | -v | -i | -e ) ] | [ -s <source root> -d <destination root> ( -a ) ]
    
    -h shows a help message.
    -i runs install_script to add the script to a folder in the $PATH.
    -l lists the license agreement.
    -s specifies source root directory.
    -d specifies source destination directory.
    -a archives the backed up folder into a tar.gz file.
    -v shows what version of backupy is running.

When a source root and destination root is specified the script will
copy all items and sub-directories from the source root into a folder
named backup<numbeer> under the destination root. If several backups
are directed to the same destination root the number in backup<number>
will increment on the new directory.

Development
-----------

At this date I am the only developer working on this project.
If you want to push some code to the project make a new folder named
backupy<version number> and put your files in there.

License
-------

This program is licensed under the GPLv3.
For more information check the supplied .txt file or go to [GNU website](http://www.gnu.org/licenses/)
