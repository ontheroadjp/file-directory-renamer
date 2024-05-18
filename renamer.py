import os
import re
import argparse

def load_patterns(pattern_file_path):
    patterns = []
    try:
        with open(pattern_file_path, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line and not clean_line.startswith("#"):  # Skip empty lines and comments
                    pattern_elements = clean_line.split('","')
                    if len(pattern_elements) == 3:
                        # Remove double quotes
                        pattern_elements = [element.strip('"') for element in pattern_elements]
                        patterns.append((pattern_elements[0], pattern_elements[1], pattern_elements[2]))
    except FileNotFoundError:
        print(f"Pattern file '{pattern_file_path}' not found.")
    return patterns

def rename_files(directory, patterns, execute=False):
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            original_path = os.path.join(root, name)
            new_name = name
            for pattern in patterns:
                if re.search(pattern[0], new_name):
                    new_name = re.sub(pattern[1], pattern[2], new_name)
            if new_name != name:
                new_path = os.path.join(root, new_name)
                if execute:
                    os.rename(original_path, new_path)
                    print(f"Renamed: {original_path} -> {new_path}")
                else:
                    print(f"Original: {original_path}, New: {new_path}")

def main():
    parser = argparse.ArgumentParser(description="Script to rename files and directories")
    parser.add_argument("directory", help="Path to the directory to be processed recursively")
    parser.add_argument("-f", "--pattern-file", default="patterns.txt", help="Path to the file containing rename patterns (default: patterns.txt)")
    parser.add_argument("-e", "--execute", action="store_true", help="Add this option to actually rename files and directories")
    args = parser.parse_args()

    pattern_file_path = args.pattern_file

    # Convert to absolute path if relative path is provided
    if not os.path.isabs(pattern_file_path):
        pattern_file_path = os.path.join(os.path.dirname(__file__), pattern_file_path)

    patterns = load_patterns(pattern_file_path)

    # Display loaded patterns
    print("Loaded patterns:")
    for pattern in patterns:
        print(pattern)

    # Rename files based on the patterns
    rename_files(args.directory, patterns, args.execute)

if __name__ == "__main__":
    main()
