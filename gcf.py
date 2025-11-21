number_1 = int(input("Please enter a whole number: "))
print(" ")
number_2 = int(input("Please enter a whole number: "))
temp_1 = number_1
temp_2 = number_2

while temp_1 != temp_2:
    if temp_1 > temp_2:
        temp_1 -= temp_2
    else:
        temp_2 -= temp_1
    
result = temp_1
print(f'{result}, is GCF of {number_1} and {number_2}')