def convert_to_uppercase(input_file, output_file):
    """
    Reads a text file, converts all text to uppercase, and saves to a new file.

    Args:
        input_file (str): Path to the input text file
        output_file (str): Path to the output text file
    """
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Convert to uppercase
        uppercase_content = content.upper()

        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(uppercase_content)

        print(f"✅ Successfully converted '{input_file}' to uppercase and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_file}' not found!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


# Example usage
if __name__ == "__main__":
    input_filename = "input.txt"  # Replace with your input file
    output_filename = "output_uppercase.txt"

    convert_to_uppercase(input_filename, output_filename)