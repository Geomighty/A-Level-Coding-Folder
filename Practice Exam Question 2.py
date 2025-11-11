ISBN = [None, ]
for i in range(1, 14):
    digit = int(input("Please enter a digit here: "))
    ISBN.append(digit)

CalculatedDigit = 0
Count = 1

while Count < 13:
    CalculatedDigit = CalculatedDigit + ISBN[Count]
    Count = Count + 1
    CalculatedDigit = CalculatedDigit + ISBN[Count] * 3
    Count = Count + 1

while CalculatedDigit >= 10:
    CalculatedDigit = CalculatedDigit - 10

CalculatedDigit = 10 - CalculatedDigit

if CalculatedDigit == 10:
    CalculatedDigit = 0

if CalculatedDigit == ISBN[13]:
   print("Valid ISBN")
else:
    print("Invalid ISBN")