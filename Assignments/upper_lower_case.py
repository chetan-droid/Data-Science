def find_string(str1):
    '''docstring! -- Find the numbers of upper and lower case in sentence
    Using isupper and islower function to find the solution
    '''
    upper_letter = 0
    lower_letter = 0
    for letter in str1:
        if letter.isupper():
            upper_letter += 1
        elif letter.islower():
            lower_letter += 1
        else:
            pass
        
    print('Original string: ', str1)
    print('No of Uppercase: ', upper_letter)
    print('No of lowercase: ', lower_letter)
    
input_string = input('Enter a string: ')
find_string(input_string)