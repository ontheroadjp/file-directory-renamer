# File and Directory Renamer

This Python script renames files and directories based on specified patterns. The script can process directories recursively and apply multiple rename patterns. It provides an option to execute the rename operations or simply preview the changes.

## Features

- Recursively process directories and rename files and directories.
- Supports multiple rename patterns specified in a pattern file.
- Allows testing rename operations without making actual changes.
- Flexible pattern matching using regular expressions.

## Usage

### Command Line Arguments

- `directory`: Path to the directory to be processed recursively.
- `-f`, `--pattern-file`: Path to the file containing rename patterns (default: `patterns.txt`).
- `-e`, `--execute`: Add this option to actually rename files and directories.

### Example Pattern File

The pattern file should contain rename patterns, each pattern on a new line. Each line should have three parts:

1. Pattern to match files or directories.
2. Pattern to match the part of the name to be replaced.
3. Replacement string.

Each part should be enclosed in double quotes and separated by commas.

#### Example `patterns.txt`

```plaintext
"NT_S1_L[0-9]{1,2}$","NT_S1_L([0-9]{1,2})","Lesson\1"
".*\.mp3$","NT1_[1-4]-[0-9]{1,2}_L[0-9]{1,2}G-","section"
".*\.mp3$","NT1_[1-4]-[0-9]{1,2}_L([0-9]{1,2})R","read\1"
```

### Running the Script

To run the script and preview the changes without actually renaming the files:

```sh
python renamer.py /path/to/directory -f /path/to/patterns.txt
```

To run the script and apply the changes:

```sh
python renamer.py /path/to/directory -f /path/to/patterns.txt -e
```

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/renamer.git
```

2. Navigate to the directory:

```sh
cd renamer
```

3. Make sure you have Python installed. This script requires Python 3.x.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs or enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the need to efficiently rename multiple files and directories in a structured manner.
