def rev_string(str1):
    rev_str = ''
    index = len(str1)

    while index > 0:
        rev_str = rev_str + str1[index - 1]
        index -= 1
        
    return rev_str

str1 = input('Enter a string: ')
print(rev_string(str1))
