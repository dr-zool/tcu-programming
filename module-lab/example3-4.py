import os
import csv

class AllFilesEmptyError(Exception):
    pass

def read_file(file_path):
    try:
        if file_path.endswith(".txt"):
            with open(file_path, 'r') as file:
                content = file.read().strip()
                if content:
                    return content.splitlines()
        elif file_path.endswith(".csv"):
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                content = list(reader)
                if content:
                    return [' '.join(row) for row in content]
        else:
            print(f"Skipping unsupported file format: {file_path}")
            return []
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except PermissionError:
        print(f"Permission denied for file: {file_path}")
        return []


def merge_files(file_list, output_file):
    all_lines = []
    for file in file_list:
        lines = read_file(file)
        all_lines.extend(lines)

    if not all_lines:
        raise AllFilesEmptyError("All files are empty!")

    try:
        with open(output_file, 'w') as out_file:
            for line in all_lines:
                out_file.write(line + '\n')
        print(f"Merged content written to {output_file}")
    except Exception as e:
        print(f"An error occurred while writing to {output_file}: {e}")

file_list = ['file1.txt', 'file2.csv', 'file3.txt']
merge_files(file_list, 'merged_output.txt')