# Example of Polymorphism in Python

class BMW:
    def start(self):
        print("BMW has started with a smooth roar.")
    
    def stop(self):
        print("BMW has stopped safely.")
    
    def fuel_type(self):
        print("BMW uses petrol or diesel.")


class Ferrari:
    def start(self):
        print("Ferrari engine starts with a powerful sound!")
    
    def stop(self):
        print("Ferrari stops quickly with ceramic brakes.")
    
    def fuel_type(self):
        print("Ferrari uses high-octane petrol.")


# Function demonstrating polymorphism
def car_test_drive(car):
    car.start()
    car.fuel_type()
    car.stop()
    print("-----------------------")


# Creating objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Calling the same method names on different objects
car_test_drive(bmw_car)
car_test_drive(ferrari_car)
