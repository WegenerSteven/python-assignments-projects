def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, welcome to python file handling module.\n")
            file.write("12345\n")
            file.write("This is another statement with some numbers: 56789\n")
        print("File created successfully!")
    except Exception as e:
        print("Error occurred while creating the file:", e)
    finally:
        file.close()


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print("Error occurred while reading the file:", e)


def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 4.\n")
            file.write("67890\n")
            file.write("This is line 6, added during appending.\n")
        print("File appended successfully!")
    except Exception as e:
        print("Error occurred while appending to the file:", e)
    finally:
        file.close()


# Create the file
create_file()

# Read and display the contents of the file
read_file()

# Append to the file
append_file()
