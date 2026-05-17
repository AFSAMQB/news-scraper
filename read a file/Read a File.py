try:
    # Step 1: Ask user for file name
    file_name = input("Enter file name (e.g. myfile.txt): ")

    # Step 2: Open the file in read mode
    with open(file_name, 'r') as file:

        # Step 3: Read everything inside
        content = file.read()

        # Step 4: Print it
        print("\nFile Content:")
        print(content)

# If file doesn't exist
except FileNotFoundError:
    print("❌ Error: File not found!")

# If no permission to open
except PermissionError:
    print("❌ Error: Permission denied!")