def create_file():
    try:
        # Create a new text file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with text and numbers: 67890\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File creation process completed.")


def read_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File reading process completed.")


def append_to_file():
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("This is line 4 (appended)\n")
            file.write("Another appended line\n")
            file.write("123456789 (appended)\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Reading file after appending to display updated content
