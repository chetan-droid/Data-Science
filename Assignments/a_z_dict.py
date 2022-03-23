#create a blank dictionary
dic = {}

#take the range from ASCII Values to get aplahabets & their values
for i in range(97,123):
    dic[chr(i)] = ord(chr(i))

print(dic)
