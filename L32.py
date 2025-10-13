# Program to swap three numbers

# Take input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print("a =", a, ", b =", b, ", c =", c)

# Swapping using temporary variable
temp = a
a = b
b = c
c = temp

print("\nAfter swapping:")
print("a =", a, ", b =", b, ", c =", c)
