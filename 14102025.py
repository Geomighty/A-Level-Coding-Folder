import math

class Vector:
    def __init__(self, x_component, y_component):
        self.x_component = x_component
        self.y_component = y_component
    
    def magnitude(self):
        self.square_x = self.x_component**2
        self.square_y = self.y_component**2
        squareroot_sum = math.sqrt(self.square_x + self.square_y)
        return squareroot_sum
    
    def __add__(self):
        added_vectors = self.x_component + self.y_component
        return added_vectors
    
    def __str__(self):
        self.x_value = f"X value: {self.x_component}"
        self.y_value= f"Y value: {self.y_component}"
        self.x_y_value = f"(x, y): ({self.y_component}, {self.x_component})"
        self.mag_of_vect = f"The magnitude = {self.magnitude()}"
        return f"{self.x_value}\n{self.y_value}\n{self.x_y_value}\n{self.mag_of_vect}\n\n"


def test_vector(vector, expected_magnitude, tolerance = 0.001):
    actual = vector.magnitude()
    if abs(actual-expected_magnitude) <= tolerance:
        print(f"{vector} magnitude is correct\n")
    else:
        print(f"{vector} magnitude is incorrect (expected {expected_magnitude})\n")
    
vector_1 = Vector(3,4)
vector_2 = Vector(7,5)
vector_3 = Vector(34, 87)
vector_4 = Vector(43, 67)
vector_5 = Vector(348, 425)
vector_6 = Vector(234, 645)

test_vector(vector_1, 5)
test_vector(vector_2, 8.60232526704)
test_vector(vector_3, 93.40770846135)
test_vector(vector_4, 79.61155694998)
test_vector(vector_5, 549.29864372671)
test_vector(vector_6, 686.13482640076)