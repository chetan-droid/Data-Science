def addition(nums):
    '''Defining additiion function to get value
    use for loop to iterate each value inside list/tuple'''
    sum_of_nums = 0

    for elements_in_list in nums:
        sum_of_nums = sum_of_nums + elements_in_list

    return sum_of_nums

nums = (8, 2, 3, 0, 7)
print(addition(nums))