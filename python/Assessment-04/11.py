# Write a Python function that sorts a list of strings based on the length of the strings


def sort_by_length(strings):
    return sorted(strings, key=len)

strings = input("Enter a list of strings separated by commas: ").split(",")
sorted_strings = sort_by_length(strings)
print("Strings sorted by length:", sorted_strings)
