# Define the Dog class
class Dog:
    # Class variable
    species = "Canis lupus familiaris"  # All dogs belong to this species

    # Constructor with two instance variables
    def __init__(self, breed, name):
        self.breed = breed   # Instance variable
        self.name = name     # Instance variable

    # Method to display dog details
    def display(self):
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("--------------------------")

# Create two dog objects of different breeds
dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("Beagle", "Charlie")

# Display details of both dogs
dog1.display()
dog2.display()
