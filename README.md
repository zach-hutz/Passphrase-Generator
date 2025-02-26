# Passphrase Generator

A simple passphrase generator implemented in Python. This project offers both a command-line interface (CLI) and a graphical user interface (GUI) using Tkinter to create secure passphrases by combining random words, symbols, and numbers.

## Features

- Generate passphrases with a customizable number of words.
- Option to include symbols and numbers.
- Customizable delimiter between words.
- CLI for quick usage.
- GUI for an interactive experience.
- Copy generated passphrase to clipboard in the GUI.

## Requirements

- Python 3
- A `wordlist.txt` file containing words (one per line) for generating passphrases.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/passphrase-generator.git
   cd passphrase-generator
   ```

## Prepare the wordlist:
Ensure that a wordlist.txt file is present in the project directory. This file should contain a list of words, one per line.

## Usage
### Command Line Interface (CLI)
Run the script with arguments to generate a passphrase:
```bash
python3 passphrase_generator.py -w 4 -s -n -d "-"
-w, --words: Number of words in the passphrase (default: 4).
-s, --symbols: Include symbols in the passphrase.
-n, --numbers: Include numbers in the passphrase.
-d, --delimiter: Delimiter to separate words (default: -).
```

### Graphical User Interface (GUI)
Run the script without any command line arguments to launch the GUI:
```bash
python3 passphrase_generator.py
```
Use the GUI to specify options and generate your passphrase. The "Copy to Clipboard" button allows you to easily copy the generated passphrase.
