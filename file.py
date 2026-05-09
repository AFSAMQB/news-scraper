def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:\n")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename to read: ")
    read_file(filename)