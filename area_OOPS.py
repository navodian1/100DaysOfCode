class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width*self.length


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))

rectangle_1 = Rectangle(a, b)
print(f"the area of rectangle :{rectangle_1.area()}")
