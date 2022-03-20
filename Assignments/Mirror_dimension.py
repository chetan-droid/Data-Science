#Get user input 

str1 = input("Enter a String: ")
str2 = ''

length = len(str1) -1
while length >= 0:
    str2 = str2 + str1[length]
    length -= 1
print(str2)