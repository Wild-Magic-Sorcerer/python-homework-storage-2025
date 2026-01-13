def save_unique_lines(input_file, output_file):
    unique_lines = set()
    non_unique_lines = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()
            if line in unique_lines:
                non_unique_lines.append(line)
            else:
                unique_lines.add(line)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in unique_lines:
            outfile.write(line + '\n')

    print("Неуникальные строки:")
    for line in non_unique_lines:
        print(line)

input_filename = 'input.txt'
output_filename = 'output.txt'
save_unique_lines(input_filename, output_filename)