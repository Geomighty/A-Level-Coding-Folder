animals = [" ", "ant", "bee", "cat", "dog", "fox"]
request = str(input("Please enter what animal you want: ")).lower()
low = 1
high = 5
#Linear Search Algorithm:
'''j = 0
found = False
while found != True or j == len(animals):
    j += 1
    if animals[j] == request:
        found = True
if found == True:
    result = j
else:
    result = 0

print(f'The animal is stored at location {result}')'''

#Binary Search Algorithm:
result = -1
while (low <= high) and (result == -1):
    middle = (low + high) // 2
    if request == animals[middle]:
        result = middle
    else:
        if request < animals[middle]:
            high = middle - 1
        else:
            low = middle + 1

print(f'The animal is stored at location {result}')