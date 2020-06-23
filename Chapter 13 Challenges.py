#Challenge 1
class Shape():
    def what_am_i(self):
        print("I am a shape.")
    
        
class Rectangle(Shape):
    pass
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculated_perimeter(self):
        return (self.width * 2) + (self.length * 2)

class Square(Shape):
    pass
    def __init__(self, s):
        self.side = s

    def calculated_perimeter(self):
        return self.side * 4

    def change_size(self, new_size):
        self.side += new_size
        

sq1 = Square(4)
print(sq1.calculated_perimeter())
rect1 = Rectangle(2, 1)
print(rect1.calculated_perimeter())

#Challenge 2 (see change_size method above)
sq2 = Square(100)
print(sq2.side)
sq2.change_size(50)
print(sq2.side)

#Challenge 3
sq1.what_am_i()
rect1.what_am_i()
sq2.what_am_i()

#Challenge 4
class Horse():
    def __init__ (self, rider, color, legs):
        self.rider = rider
        self.color = color
        self.legs = legs

class Rider():
    def __init__(self, name):
        self.name = name

steve = Rider("Steve")
neighdra = Horse(steve, "Chesnut", 4)
print(neighdra.rider.name)

jones = Rider("Jones")
kit = Horse(jones, "Black", 3)
print(kit.rider.name)

mac = Rider("Mac")
bessy = Horse(mac, "Dapple", 3)
print(bessy.color)

    

        
