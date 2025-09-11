name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']
for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print(name_list)
print(" ")
print(f"The third name is: {name_list[2]}")
print(" ")
print(f"The last seven names are: {name_list[-7:]}")
print(" ")
number_list = []
for i in range(5):
    number = int(input("Please enter a integer: "))
    number_list.append(number)
print(" ")
print(f"The largest number is: {max(number_list)}")
print(" ")
print(f"The smallest number is: {min(number_list)}")
print(" ")
print(f"The total off all the numbers in the list is: {sum(number_list)}")
print(" ")
print(f"The mean of all the numbers is: {(sum(number_list))/(len(number_list))}")