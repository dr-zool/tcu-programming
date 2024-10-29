# Open input and output files
input_file = open("../example2/input.txt", "r")
output_file = open("../example2/output.txt", "w")

# Process each line in the input file
for line_str in input_file:
    new_str = ''
    line_str = line_str.strip()  # Remove any trailing newline or whitespace
    for char in line_str:
        new_str = char + new_str  # Prepend characters to reverse the string
    print(new_str, file=output_file)  # Write the reversed string to output file

    # Print progress to the console
    print(f'Line: {line_str:12s} reversed is: {new_str}')

# Close the input and output files
input_file.close()
output_file.close()
