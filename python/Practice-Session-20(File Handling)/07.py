# 7. Write a script that takes a file name as input and prints the number of lines, words,
# and characters in the file.

try:
    file_name = input("Enter the file name: ")
    with open(fr"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\{file_name}", 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_characters = sum(len(line) for line in lines)
    print(f"Number of Lines: {num_lines}")
    print(f"Number of Words: {num_words}")
    print(f"Number of Characters: {num_characters}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

