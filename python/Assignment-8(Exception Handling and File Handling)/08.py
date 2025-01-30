# 8.	Create a class FileProcessor with methods to:
# •	Read a file.
# •	Write to a file.
# •	Append data to a file.

class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                print(f"Content of {self.filename}:")
                print(content)
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied when trying to read the file '{self.filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")

    def write_file(self, content):
        try:
            with open(self.filename, 'w') as file:
                file.write(content)
                print(f"Content has been written to {self.filename}.")
        except PermissionError:
            print(f"Error: Permission denied when trying to write to the file '{self.filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")

    def append_to_file(self, content):
        try:
            with open(self.filename, 'a') as file:
                file.write(content)
                print(f"Content has been appended to {self.filename}.")
        except PermissionError:
            print(f"Error: Permission denied when trying to append to the file '{self.filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred while appending to the file: {e}")

filename = input("Enter the filename: ")
processor = FileProcessor(filename)

processor.read_file()

content_to_write = input("Enter content to write to the file: ")
processor.write_file(content_to_write)

content_to_append = input("Enter content to append to the file: ")
processor.append_to_file(content_to_append)
