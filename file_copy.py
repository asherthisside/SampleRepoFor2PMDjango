# fp = open("mydata.txt", '')
# f_data = fp.read()
# fp.write("This is some random text")
# fp.close()
# print(f_data)

# fp = open('mydata_copy.txt', 'w')
# fp.write(f_data)
# fp.close()

# Explore how does r+ work.
# Assignment: Write a program to cut the data from a file and paste into another. 

# Appending into a file
fp = open('pythonFile.txt', 'a')
# fp.write("\nI added this 6th line with the help of python.")
# fp.write("\nPython helped me to add this 7th line as well.")
fp.seek(60)
fp.readline()
# fp.write("THIS IS APPENDED IN THE MIDDLE")