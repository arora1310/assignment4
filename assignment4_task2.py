file_name="output.txt"
file1= open('output.txt','wt')
first_input=input("Enter text to write to the file named output.txt:")
write_file=file1.write(first_input)
file1.close()
print(f"data successfully written to {file_name}.")

file2=open(file_name,'at')
second_input=input("Enter additional text to append:")
appending_file=file2.write("\n"+second_input)
print("data successfully appended")
file2.close()

print(f"Final content of {file_name} is:")
file3=open(file_name,'rt')
final=file3.read()
print(final)
file3.close()




