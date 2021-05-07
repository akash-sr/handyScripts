"""
Descritption:   Python script to setup files for Codeforces contests.
                Suppose you are participating in Codeforces Round #720 (Div 2).
                This script will create files like 720a.cpp, 720b.cpp, ... using your codeforces template.
"""

import os
import shutil

# set the parent folder path where you want to create your files
parent = "D:\\CP\\Codeforces"

# set constest number. add a suffix 'ed' if the round is educational
contestNo = input("Enter contest no. (write ed<contest_no> if it is an educational round): ")
# set the number of files you want to create
fileCount = int(input("Enter no. of problems you think you can solve :) -"))

# set the path for your template
template = f"{parent}\\template.txt"

# do the deed
while fileCount > 0:
    shutil.copyfile(template,f"{parent}\\{contestNo}{chr(fileCount+96)}.cpp")
    fileCount-=1
