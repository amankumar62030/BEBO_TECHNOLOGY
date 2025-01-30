# Write a function called to_title_case that converts a string to title case (i.e., the first letter of each word should be uppercase).

def to_title_case(n):
    words = n.split()
    return ' '.join(word.capitalize() for word in words)



n = input("Enter any String: ")
result = to_title_case(n)
print(result)