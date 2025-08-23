import math

number=int(input("Enter a number: "))

if number >= 0:
    sqrt=math.sqrt(number)
    print(f"The square root of {number} is {sqrt}")
else:
    print("Sorry, square root of a negative number is not real.")
    