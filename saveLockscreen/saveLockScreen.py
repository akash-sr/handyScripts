"""
Descritption: Python script to save Windows Lockscreen images to desired folder
"""

import shutil
import os
import sys
# get user porfile name
userprofile = os.getlogin()
# set the source where Lockscreen images are saved by default **Do Not Change This**
src = f"C:\\Users\\{userprofile}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
# set the Folder where you want to save the Lockscreen images
dest = "D:\\Lockscreen"

# get file names of images
fileList = os.listdir(src)

# copy all these files to the destination and append .jpg to change file extension
for files in fileList:
    shutil.copyfile(f"{src}\\{files}",f"{dest}\\{files}.jpg")

# Voila!
