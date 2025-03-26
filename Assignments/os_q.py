import os
import time

files=os.listdir("C://Users//Admin//PycharmProjects//PythonProject1//my_package")

for i in files:
    # file_path = os.path.abspath(i)
    path=os.path.join("C://Users//Admin//PycharmProjects//PythonProject1//my_package",i)
    stats = os.stat(path)
    # print(stats)
    creation_time = os.path.getctime(path)
    creation_time = time.ctime(creation_time)
    print(f"{i} module created on: {creation_time}")

