# 10.	Create a function process_file(file_path) that reads a file and returns the total number of words
# in it. Handle exceptions for missing file, empty file, and encoding errors.

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:
                print("The file is empty.")
                return 0
            words = content.split()
            return len(words)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return 0

    except IOError:
        print(f"Error: There was an issue reading the file '{file_path}'.")
        return 0

    except UnicodeDecodeError:
        print(f"Error: Encoding error while reading the file '{file_path}'.")
        return 0

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

file_path = input("Enter the path of the file: ")
word_count = process_file(file_path)
if word_count != 0:
    print(f"The total number of words in the file is: {word_count}")
