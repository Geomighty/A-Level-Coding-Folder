number_of_numbers = int(input("How many digits would you like to enter"))
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(number_of_numbers):
    number = int(input("Enter your digit here: "))
    if number == 0:
        numbers[0] = numbers[0] + 1
    elif number == 1:
        numbers[1] = number[1] + 1
    elif number == 2:
        numbers[2] = number[2] + 1
    elif number == 3:
        numbers[3] = number[3] + 1
    elif number == 4:
        number[4] = number[4] + 1
    elif number == 5:
        number[5] = number[5] + 1
    elif number == 6:
        number[6] = number[6] + 1
    elif number == 7:
        number[7] = number[7] + 1
    elif number == 8:
        number[8] = number[8] + 1
    elif number == 9:
        number[9] = number[9] + 1
count = 0
for i in range(len(numbers)):
    if numbers[i] > count:
        count = i
    elif numbers[i] < count:
        count = count
    else:
        count = "Data is multimodal"

if count == int:
    print(f"the digit entered most was: {count}")
else:
    print(count)