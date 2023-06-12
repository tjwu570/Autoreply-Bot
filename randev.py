import random

input_file = '/home/chinlin/Documents/dlpifp/data/dev.txt'
output_file = '/home/chinlin/Documents/dlpifp/data/dev2.txt'

# Count the number of lines in the input file
with open(input_file, 'r') as file:
    line_count = sum(1 for line in file)

num_lines = 200

# Check if the input file has enough lines for sampling
if line_count < num_lines:
    print("Error: The input file doesn't have enough lines.")
    exit()

# Generate a list of random line numbers to sample
line_numbers = random.sample(range(1, line_count + 1), num_lines)

selected_lines = []
with open(input_file, 'r') as file:
    for i, line in enumerate(file, start=1):
        if i in line_numbers:
            selected_lines.append(line)

# Save the selected lines to the output file
with open(output_file, 'w') as file:
    file.writelines(selected_lines)

print(f"Randomly selected {num_lines} lines from {input_file} and saved to {output_file}.")
