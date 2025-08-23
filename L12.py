base=int(input("enter the base's value"))
power=int(input("Enter the power's value"))
ans=1
for i in range(power):
    ans=ans*base
print(f"the {base} to the power {power} is {ans}")
