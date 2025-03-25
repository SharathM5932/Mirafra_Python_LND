# file handling-w+,seek(),os ,path , convert to json, del path, zip,
# move,.realpath, exists., copy, shutil.make_archive, file socket
import os
# file1=open("anuroop.txt",'a')
# file1.write("\nMy name is anuroop2")
# file1.close()

# file1=open("anuroop.txt",'r')
# print(file1.readline())
#
# from os import path
# print(path.exists('anuroop.txt'))
# file1.seek(1)

# file socket

# HW
from os import path
# files=os.listdir("PT0601day1")
# for files in os.listdir("PT0601day1"):
#     timestamp=os.path.getmtime(files)
#     print(files,timestamp)

import datetime
print("file name","----------","time of creation")
for file in os.listdir("PT0601day1"):
    # print(file)
    path1=os.path.join("G:\My Drive\Mirafra\TRAINING\PYTHON_TRAINING\PYTHON_TRAINING\PT0601day1",file)
    fileinfo=os.stat(path1)
    print(fileinfo)
    creation_time=datetime.datetime.fromtimestamp(fileinfo.st_ctime)
    print(file,"-------------",creation_time)
