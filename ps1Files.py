def filter_ps1_lines(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            # Read all lines from the input file
            lines = input_file.readlines()

            # Filter lines ending with .ps1
            ps1_lines = [line.strip() for line in lines if line.strip().endswith('.ps1')]

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Write filtered lines to the output file
            for ps1_line in ps1_lines:
                output_file.write(ps1_line + '\n')

        print(f"Filtered lines written to {output_file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_file_path = 'directoryListing.txt'  # Replace with your input file path
output_file_path = 'ps1Files.txt'  # Replace with your output file path

filter_ps1_lines(input_file_path, output_file_path)
