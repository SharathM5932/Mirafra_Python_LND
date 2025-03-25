"""f1=open("Deepika.txt")
f2=open("Neha.txt")"""

"""f1.close()
f2.close()
with open("Deepika.txt") as d,open("Neha.txt") as n:
    print(d.read())
    print(n.read())"""

"""for i,j in zip(f1,f2):
    a=i.title()
    b=j.upper() 
    print(a)
    print(b)"""
"""f=open("Zipped_files.txt",'w+')
f=zip(f1,f2)
f1.close()
f2.close()"""

"""import zipfile
file1="Deepika.txt"
file2="Neha.txt"
zip_filename="my_files.zip"
with zipfile.ZipFile(zip_filename,'w') as zipf:
   zipf.write(file1)
   zipf.write(file2)

print(f"{zip_filename} created successfully!")"""


"""count=0
for line in open('Neha.txt').readlines(): count+=1
print(count)"""

"""f1=open('Deepika.txt','w')
with open('Neha.txt','r') as myfile:
   data=myfile.read()
   data_1=data[::-1]
   f1.write(data_1)
   print(f1)
f1.close()
"""

"""import json
a=open('lakshmi.txt','w+')
a.write('''Python too supports file handling and allows users to 
handle files i.e., to read and write files, along with many other 
file handling options, to operate on files. ... Python treats file 
differently as text or binary and this is important. 
Each line of code includes a sequence of characters and 
they form text file.''')
a.close()
with open('lakshmi.txt','r') as my:
    data=my.read()
with open('lakshmi.txt') as f:
    output=open('likitha.json','w')
    for l in f:
        d=list(l.strip().split())
        json.dump(d,output)
        output.write('\r\n')
output.close()"""


import json
a=open("Sample.txt",'w')
a.write("HDDCHDHHDSJDSKJDSJSJSKLK CDGCIICDIDID KDGUIHCKC<C<MC")
a.close()
with open("Sample.txt") as s:
   x=s.read()
