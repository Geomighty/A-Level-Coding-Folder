name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']
for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print(name_list)
print(" ")
print(f"The third name is: {name_list[2]}")
print(" ")
print(f"The last seven names are: {name_list[11:18]}")
print(" ")
number_list = []
for i in range(5):
    number = int(input("Please enter a integer: "))
    number_list.append(number)
number_list.sort()
total = 0
for i in range(5):
    total = total + number_list[i]
mean = total/5
print(f"The largest number is: {number_list[4]}")
print(" ")
print(f"The smallest number is: {number_list[0]}")
print(" ")
print(f"The total off al the numbers in the list is: {total}")
print(" ")
print(f"The mean of all the numbers is: {mean}")