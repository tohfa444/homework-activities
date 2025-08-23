import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


r = float(input("Enter the radius of the circle: "))
c = Circle(r)

print(f"Area of circle: {c.area():.2f}")
print(f"Circumference of circle: {c.circumference():.2f}")
