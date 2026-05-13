def process_file(input_file,output_file):
    try:
        with open(input_file,"r") as infile:
            with open(output_file,"w") as outfile:
                for line in infile:
                    processed_data = line.upper()
                    outfile.write(processed_data)

        print("File Processed Successfully")

    except FileNotFoundError:
        print("Input File Not Found")

process_file("input.txt","output.txt")