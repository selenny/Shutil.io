#!/user/bin/python
# Python Ver:     2.7
#
# Author:	      Terri Hall
#
# Purpose:	       Create a program that will move .txt files from one folder to another with a click of a button.
#
# Tested OS:       This code was written and tested to work with Windows 10.
 

import shutil
import os


src = 'C:\Users\webde\Desktop\FolderA'
dest = 'C:\Users\webde\Desktop\FolderB'
print src
print dest

file_Names = os.listdir(src)
print file_Names

for file in file_Names:
    if file.endswith(".txt"):
        shutil.move(src + '/'+ file, dest)
    else:
        print("Files cannot be moved at this time")
                  
                   
               
