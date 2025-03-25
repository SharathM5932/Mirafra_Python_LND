import os
from datetime import datetime
directory='.'
files=os.listdir(directory)
print(files)
print(len(files))
fileinfo=[]
for i in files:
    filepath=os.path.join(directory,i)
    if os.path.isfile(filepath):
        creation_time = os.path.getctime(filepath)
        creation_time_str = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        fileinfo.append((i, creation_time_str))
for i,creation_time in fileinfo:
    print(f"Filename: {i}, Created: {creation_time}")

    print(f"\nTotal number of files: {len(fileinfo)}")
