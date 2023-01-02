# File pointer - 
# Absolute path - C:\Users\Admin\Desktop\GitCommands.txt
# Relative path ../../text_files/python/GitCommands.txt

fp = open('../GitCommands.txt', 'r')
file_data = fp.read()
# print(len(file_data))
fp.close()

# print(file_data)

# Writing into a file. 
# w - Writing only mode. 

fp = open('mydata.txt', 'w')
fp.write(file_data)

# Write a program to copy a file content into another.