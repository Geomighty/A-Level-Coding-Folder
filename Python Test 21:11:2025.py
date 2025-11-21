#Question 1:
'''x = int(input("enter an integer that is > 1: "))
product = 1
factor = 0
while product < x:
    factor = factor + 1
    product = product * factor
if x == product:
    product = 1
    for n in range(1, (factor + 1)):
        product = product * n
        print(n)
else:
    print("no result")'''

#Question 2
word_1 = str(input("Please enter a word here in all capitals: "))
word_2 = str(input("Please enter a word here in all capitals: "))

word_1_list = list(word_1)
word_2_list = list(word_2)
counter = 0

if len(word_1_list) > len(word_2_list):
    print(f'{word_1} cannot be made from {word_2} as it has more letters than {word_2}')
else:
    for i in range(len(word_2_list)):
        word_2_list_letter = word_2_list[i]
        number_of_letter_word_2 = word_2_list.count(word_2_list_letter)
        number_of_letter_word_1 = word_1_list.count(word_2_list_letter)
        if number_of_letter_word_2 >= number_of_letter_word_1:
            counter += number_of_letter_word_1
            word_1_list.remove(word_2_list_letter)
        else:
            counter = counter

if counter == len(word_1_list):
    print(f'{word_1} can be made from {word_2}')
else:
    print(f'{word_1} cannot be made from {word_2} as there are insufficent matching letters')