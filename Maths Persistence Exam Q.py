value = int(input("Please enter an integer between 0 and 99: "))
operation = str(input("Calculate additive or multiplicative persistence (a or m)")).lower()
count = 0
while value > 9:
    if operation == "a":
        value = (value//10) + (value%10)
    else:
        value = (value//10) * (value%10)
count += 1
print(f'The persistence is: {count}')
