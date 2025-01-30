def reverse_characters_in_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


sentence = input("Enter a sentence: ")
print("Sentence with words reversed:", reverse_characters_in_words(sentence))




