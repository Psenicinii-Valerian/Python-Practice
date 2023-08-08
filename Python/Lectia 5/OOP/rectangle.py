class Rectangle:
    a = 7
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 10)
rect2 = Rectangle(10, 20)

print(rect2.a)
print(rect1.get_perimeter())
print(rect1.get_area())
print(rect2.get_perimeter())
print(rect2.get_area())