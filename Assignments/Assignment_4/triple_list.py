
def triple_the_list(nums):
    '''This fucntion dervies that it will triplets the numbers
    inside a list
    Using list input'''
    return nums * 3

#Take input as list
num = eval(input("Enter a list: "))

results = map(triple_the_list, num)
print(list(results))