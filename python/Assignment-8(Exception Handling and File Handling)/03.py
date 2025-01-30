# 3.	Write a function that opens a file, writes a list of numbers (1 to 10) into the file,
# and then closes it. Use a try-finally block to ensure the file is properly closed even if an
# exception occurs.

def write_numbers_to_file(numbers):
    try:
        file = open(r"D:\BEBO TECHNOLOGY\python\Assignment-8(Exception Handling and File Handling)\numbers.txt", 'w')

        for number in range(1, 11):
            file.write(f"{number}\n")
        print(f"Numbers 1 to 10 have been written to {numbers}.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        file.close()
        print("File has been closed.")


write_numbers_to_file("numbers.txt")

