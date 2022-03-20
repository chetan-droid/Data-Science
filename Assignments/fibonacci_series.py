#Get user input as range of fibonacci series 
num = int(input("Enter a range of number: "))
x,y = 0,1

while y < num:
    print(y, end=' ')
    x,y = y,x+y