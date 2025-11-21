'''def hash(key):
    sum = 0
    for i in range(len(key)):
        sum = sum + ord(key[i]) * ord(key[i])
    hash = sum % 523
    return hash

print(hash("PEN"))
print(hash("CAT"))
print(hash("NOW"))
print(hash("WON"))'''

# Programming Tasks P289 Bond Textbook 1

values_list = []
for i in range(523):
    values_list.append("-1")

addresses = []

def hash_storing(key):
    sum = 0
    for i in range(len(key)):
        sum = sum + ord(key[i]) * ord(key[i])
    hash = sum % 523
    addresses.append(hash)

english_french_list = [["PEN", "PLUME"], ["CAT", "CHAT"], ["NOW", "MAINTENANT"]]

for d in range(3):
    hash_storing(english_french_list[d][0])

for j in range(3):
    values_list[addresses[j]] = english_french_list[j]

for h in range(3):
    print(f'{english_french_list[h]} is stored at {values_list.index(english_french_list[h])} address in the values list')

def hash_retriving(key):
    sum = 0
    for i in range(len(key)):
        sum = sum + ord(key[i]) * ord(key[i])
    hash = sum % 523
    return hash

user_english_word = str(input("Please enter in all capitals the word you want to find the french for enter STOP to quit: "))

while user_english_word != "STOP":
    print(f'The french for {user_english_word} is {values_list[hash_retriving(user_english_word)][1]}')
    user_english_word = str(input("Please enter in all capitals the word you want to find the french for enter STOP to quit: "))