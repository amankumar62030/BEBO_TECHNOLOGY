# 7.	Create a script to copy content from one file to another. Handle exceptions for missing source
# file, permission errors, and other unforeseen issues.

def copy_file_content(source_file, destination_file):
    try:
        source = open(r"D:\BEBO TECHNOLOGY\python\Assignment-8(Exception Handling and File Handling)\file1.txt", 'r')
        destination = open(r"D:\BEBO TECHNOLOGY\python\Assignment-8(Exception Handling and File Handling)\file2.txt", 'w')
        content = source.read()
        destination.write(content)
        print(f"Content successfully copied from {source_file} to {destination_file}.")

    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' does not exist.")

    except PermissionError:
        print(f"Error: Permission denied. Unable to write to the file '{destination_file}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        try:
            source.close()
        except NameError:
            pass
        try:
            destination.close()
        except NameError:
            pass

source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")
copy_file_content(source_file, destination_file)
