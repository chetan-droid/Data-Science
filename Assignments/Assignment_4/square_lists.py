def square_the_list(nums):
    '''This fucntion squares the numbers inside a list'''
    return nums ** 2

#Take input as list
num = eval(input("Enter a list: "))

result = map(square_the_list, num)
print(list(result))