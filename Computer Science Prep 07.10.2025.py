import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = ((2*self.width) + (2*self.height))
        return perimeter

    def get_diagonal(self):
        hypotenuse = math.sqrt((self.width**2) + (self.height**2))
        return hypotenuse

rectangle_1 = Rectangle(3, 4)
rectangle_2 = Rectangle(5, 7)
rectangle_3 = Rectangle(38, 96)
rectangle_4 = Rectangle(556, 887)
rectangle_5 = Rectangle(8496, 6295)
rectanlges_area = [12, 35, 3648, ]

rectangles = [rectangle_1, rectangle_2, rectangle_3, rectangle_4, rectangle_5]

print("The following rectangles with their measurements are going to be used to test the code")
print(" ")
print("Rectanlge 1 = 3X4")
print("Rectangle 2 = 5X7")
print("Rectanlge 3 = 38X96")
print("Rectanlge 4 = 556X887")
print("Rectangle 5 = 8496X6295")
print(" ")
print(" ")

for i in range(5):
    print(f"Rectangle {i+1}:")
    print(" ")
    print(f"Area = {rectangles[i].get_area()}")
    print(f"Perimetre = {rectangles[i].get_perimeter()}")
    print(f"Hypotenuse = {rectangles[i].get_diagonal()}")
    print(" ")
    print(" ")