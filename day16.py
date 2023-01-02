# Email Slicer
# shibna@havefurn.com 
####################### Method 1 ###########################
# usermail = input("Enter your Email ID: ")
# username = usermail[0:usermail.index('@')]
# domain_name = usermail[usermail.index('@') + 1:]
# print(f"Username: {username}\nDomain name: {domain_name}")

######################## Method 2 ###########################
usermail = "shibna@havefurn.com"
username_list = []
domain_list = []
for i in usermail:
    if i == '@':
        break
    username_list.append(i)

for i in range(usermail.index('@') + 1, len(usermail)):
    domain_list.append(usermail[i])
    # print(i)
    
username = "".join(username_list)
domain = "".join(domain_list)
# print(username)
# print(domain)


# open(filename, mode)
fp = open('pythonFile.txt', 'r')
# print(fp.read(45))

# print(fp.tell())
# fp.seek(60)
# print(fp.read(30))
# print(fp.readline())
# print(fp.readline())
# print(fp.readline())

# print first line of the text 15 times. 
# for i in range(1, 16):
#     print(fp.readline())
#     fp.seek(0)

# line1 = fp.readline()
# print(line1 * 10)
print(fp.readlines())