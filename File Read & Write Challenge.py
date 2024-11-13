# Function to read from a file, modify its content, and write to a new file
def modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the content of the file

        # Modify the content (for example, converting text to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue with reading or writing to the file.")

# Function to ask for a filename and handle errors if the file doesn't exist or can't be read
def read_file_with_error_handling():
    filename = input("Please enter the filename you want to read: ")

    try:
        # Try opening the file and reading its content
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")

# Main driver code
def main():
    # File Read & Write Challenge
    input_filename = "input.txt"  # Replace with your input file name
    output_filename = "output.txt"  # The new file where modified content will be saved
    modify_file(input_filename, output_filename)

    # Error Handling Lab
    read_file_with_error_handling()

if __name__ == "__main__":
    main()
