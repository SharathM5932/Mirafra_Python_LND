'''# Open a file in read mode
file = open('example.txt', 'w+')
for _ in range(5):
    file.writelines("hello,world\n")
file.seek(0)
# Read the first 5 characters
content = file.read(5)
print('Content:', content)
# Check the current position
position = file.tell()
print('Current Position:', position)
# Move the pointer to the 10th byte from the start
file.seek(0)
print('Position after seeking to 10th byte:', file.tell())
# Read the next 5 characters
content = file.readlines(20)
print('Content after seeking:', content)
file.close()'''

#2
# Open a file in  read mode
'''file = open('example.txt', 'r')
count=0
for i in file:  # Iterates over each line in the file
    for j in i:  # Iterates over each character in the line
        if j.isalpha():  # Checks if the character is a letter
            count += 1
print(count)
file.close()'''

#3

