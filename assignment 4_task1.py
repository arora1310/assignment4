import os

file_name= "sample.txt"

if os.path.exists(file_name):
    file= open('sample.txt','r')
    line1=file.readline()
    line2=file.readline()
    line3=file.readline()
    print(line1)
    print(line2)
    print(line3)
    file.close()
else:
    print(f"Error:The file '{file_name}' was not found")