import math
'''class Thing:
    def __init__(self):
        self.x = 10
    
    def __str__(self):
        return "A thing"
    
    def __repr__(self):
        return "a thing in debug mode"

thing = Thing()
print(thing)'''

class Vector:
    def __init__(self, x_component, y_component):
        self.x_component = x_component
        self.y_component = y_component
    
    def magnitude(self):
        self.square_x = self.x_component**2
        self.square_y = self.y_component**2
        squareroot_sum = math.sqrt(self.square_x + self.square_y)
        return squareroot_sum
    
    def __str__(self):
        self.x_value = f"X value: {self.x_component}"
        self.y_value= f"Y value: {self.y_component}"
        self.x_y_value = f"(x, y): ({self.y_component}, {self.x_component})"
        self.mag_of_vect = f"The magnitude = {self.magnitude()}"
        return f"{self.x_value}\n{self.y_value}\n{self.x_y_value}\n{self.mag_of_vect}\n"
    
vector = Vector(3, 4)
print(vector)