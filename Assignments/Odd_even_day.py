#Get user input for days
days = int(input("Enter number of total days: "))
even = 0
odd = 0

for i in range(1, days + 1):
    
    if i%2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Number of even days: ",even)
print("Number of odd days: ",odd)

