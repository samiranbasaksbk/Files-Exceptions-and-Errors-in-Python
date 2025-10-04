# Task 2: Write and Append Data to a File

# Step 1: Write user input to a file
user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
with open("output.txt", "a") as file:
    file.write("This line was appended to the file.\n")

# Step 3: Read and display the final content
print("\nFinal content of 'output.txt':\n")
with open("output.txt", "r") as file:
    print(file.read())
