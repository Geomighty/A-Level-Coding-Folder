file_contents: str = open('bee20script.txt', 'r').read()

file_contents = file_contents.replace(',', '')
file_contents = file_contents.replace('.', '')
file_contents = file_contents.replace('-', '')
file_contents = file_contents.replace('?', '')
file_contents = file_contents.replace('!', '')
file_contents = file_contents.lower() 
word_list = file_contents.split() 

word_frequency = {word : word_list.count(word) for word in word_list}
word_frequency = sorted(word_frequency, key = word_frequency.get, reverse=True)
print(word_frequency)