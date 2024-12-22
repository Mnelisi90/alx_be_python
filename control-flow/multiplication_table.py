# define variable and prompt user to input number
number = int(input("Enter a number to see its multiplication table:"))

#generate loop
for i in range(1,11): #loop from 1 to 11
    result = number * i
   print(f"{number} * {i} = {result}")
