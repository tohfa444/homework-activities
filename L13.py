n=int(input("Enter your number"))
c=0
while n>0:
    n=n//10
    c+=1
print("The number of digit of this inteeger is ",c)
