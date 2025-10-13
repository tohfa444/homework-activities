# Program to check the ASCII value of a given character

# Take input from user
char = input("Enter a character: ")

# Check if user entered exactly one character
if len(char) == 1:
    print("The ASCII value of", char, "is:", ord(char))
else:
    print("Please enter only one character!")
