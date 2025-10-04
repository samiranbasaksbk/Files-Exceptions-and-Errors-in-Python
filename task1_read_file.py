# Task 1: Read a File and Handle Errors

try:
    # Attempt to open and read the file
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
