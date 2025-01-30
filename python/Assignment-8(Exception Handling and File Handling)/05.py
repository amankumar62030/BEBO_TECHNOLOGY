# 5.Create a Python program that takes a filename as input and writes user-provided data into it. Handle exceptions for:
# •	Invalid filename input (e.g., blank filename).
# •	Permission denied when writing to the file.

def write_to_file():
    try:
        file_name = input("Enter the filename to write data into: ").strip()

        if not file_name:
            raise ValueError("Filename cannot be blank.")

        file = open(file_name, 'w')
        data = input("Enter the data to write into the file: ")
        file.write(data)
        print(f"Data has been successfully written to {file_name}.")

    except ValueError as ve:
        print(f"Error: {ve}")

    except PermissionError:
        print(f"Error: Permission denied. Unable to write to the file {file_name}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        try:
            file.close()
        except NameError:
            pass

write_to_file()

