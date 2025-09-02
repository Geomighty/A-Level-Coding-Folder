multiplication_table = int(input("enter the number of the multiplication table you would like"))
multiples = int(input("enter the number of multiples of that number you would like to know"))
results = []
for i in range(multiples):
    multiplication_results = multiplication_table * (i+1)
    results.append(multiplication_results)
for j in range(multiples):
    print(f"{multiplication_table} X {j + 1} = {results[j]}")