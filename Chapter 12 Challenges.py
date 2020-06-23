import math

#Challenge 1
class Apple():
    def __init__(self, w, c, f, v):
        self.weight = w
        self.color = c
        self.flavor = f
        self.variety = v
        print("New Apple!")

apple1 = Apple(2.1, "Red", "Tart", "Jonathan")
apple2 = Apple(3.1, "Green", "Tart", "Granny Smith")
apple3 = Apple(2.4, "Red", "Crisp", "Red Delicious")
print(apple1.color)
print(apple2.variety)
print(apple3.flavor)


#Challenge 2
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (self.radius * math.pi) ** 2

    def diameter(self):
        return self.radius * 2

    def circumference(self):
        return (self.radius * 2) * math.pi

circ1 = Circle(1)
print(circ1.area())

circ2 = Circle(4)
print(circ2.diameter())
print(circ2.circumference())


#Challenge 3
class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height)/2

triangle = Triangle(10, 1)
print(triangle.area())


#Challenge 4
class Hexagon():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6

hex1 = Hexagon(6)
print(hex1.calculate_perimeter())
