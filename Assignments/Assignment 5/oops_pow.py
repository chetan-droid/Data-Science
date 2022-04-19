import math
'''Importing math module to use power function
'''
class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def nth_power(self):
        
        return f'The output is {math.pow(self.x, self.n)}'

x = int(input('Enter a x number : '))
n = int(input('Enter a n number : '))    
obj = Power(x,n)

print(obj.nth_power())