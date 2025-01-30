n = input("Enter the string: ")

longest_word = n.split()
length = 0

for word in longest_word:
    if len(word) > length:
        length = len(word)
print("longest length of word is",length)