import os
import time
dir_path = r'C:\Users\Admin\PycharmProjects\PythonProject1\module1'

for file in os.listdir(dir_path):
    file_path=os.path.join(dir_path,file)

    if os.path.exists(file_path):
        creation_time = os.path.getctime(file_path)
        creation_time_str = time.ctime(creation_time)
    print(f'File: {file} - Creation Time: {creation_time_str}')
