sentence = "aeiou"
vowels = ["a", "e", "i", "o", "u"]
number = 0

def get_count(sentence):
    sentence_list = list(sentence)
    number += sentence_list.count(vowels[0])
    print(f'the number of vowels is: {number}')
print(get_count(sentence))