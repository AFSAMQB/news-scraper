def process_file(input_file, output_file):
    try:
        # Open input file to read
        with open(input_file, 'r') as infile:
            # Open output file to write
            with open(output_file, 'w') as outfile:
                # Go line by line
                for line in infile:
                    # Convert each line to UPPERCASE
                    processed = line.upper()
                    # Write it to output file
                    outfile.write(processed)

        print("✅ File processed successfully!")

    except FileNotFoundError:
        print("❌ Input file not found!")

# Run the function
process_file('input.txt', 'output.txt')