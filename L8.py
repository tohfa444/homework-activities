Character=input("Enter your character ")

if len(Character)==1:
    if Character.isalpha():
        print("This is an alphabetical letter")
    else:
        print("This is not an alphabetical letter")
else:
    print("Please enter a singel character")