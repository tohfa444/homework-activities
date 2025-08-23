class BMW:
    def start(self):
        print("BMW engine started.")

    def speed(self):
        print("BMW top speed is 250 km/h.")


class Ferrari:
    def start(self):
        print("Ferrari engine started.")

    def speed(self):
        print("Ferrari top speed is 350 km/h.")

bmw_car = BMW()
ferrari_car = Ferrari()

for car in (bmw_car, ferrari_car):
    car.start()
    car.speed()
    print()  
    
