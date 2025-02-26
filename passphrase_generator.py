# Define imports
import random
import tkinter as tk
from tkinter import ttk
import argparse
import sys

# Define symbols variables since I don't want to include every single symbol in the string module.
symbols = ["/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "{", "}", "[", "]", "\\", ":", ";", "<", ">", "?", "~"]

def generate_passphrase(num_words=4, add_symbols=True, add_numbers=True, delimiter='-'):
    # Load the words from an external file.
    with open('wordlist.txt', 'r') as f:
        words = [word.strip() for word in f if word.strip().isalpha()]
   
    # Select random words.
    passphrase_list = [random.choice(words) for _ in range(num_words)]

    # Capitalize random words in the passphrase.
    if random.choice([True, False]):
        randChoice = random.choice(range(num_words))
        passphrase_list[randChoice] = passphrase_list[randChoice].upper()
    
    # Modify a randomly selected word (except the last) to include a symbol.
    if add_symbols:
        randChoice = random.choice(range(num_words - 1)) if num_words > 1 else 0
        symbol = random.choice(symbols)
        if random.choice([True, False]):
            passphrase_list[randChoice] = symbol + passphrase_list[randChoice]
        else:
            passphrase_list[randChoice] = passphrase_list[randChoice] + symbol

    # Modify a randomly selected word (except the last) to include a number.
    if add_numbers:
        randChoice = random.choice(range(num_words - 1)) if num_words > 1 else 0
        number = str(random.randint(0, 9))
        if random.choice([True, False]):
            passphrase_list[randChoice] = number + passphrase_list[randChoice]
        else:
            passphrase_list[randChoice] = passphrase_list[randChoice] + number

    return delimiter.join(passphrase_list)

# This function creates the command line interface for the passphrase generator.
def cli_interface():
    # Create the argument parser.
    parser = argparse.ArgumentParser(description='Generate a secure passphrase')

    # Words argument
    parser.add_argument('-w', '--words', type=int, default=4, help='Number of words in the passphrase')

    # Symbols argument
    parser.add_argument('-s', '--symbols', action='store_true', help='Include symbols in the passphrase')

    # Numbers argument
    parser.add_argument('-n', '--numbers', action='store_true', help='Include numbers in the passphrase')

    # Delimiter argument
    parser.add_argument('-d', '--delimiter', type=str, default='-', help='Delimiter between elements in the passphrase')

    # Parse the arguments (ARGGGGG)
    """
    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⣠⣤⣶⣶⣿⣿⣿⣿⣯⠀⠀⣽⣿⣿⣿⣿⣷⣶⣤⣄⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⡅⠉⠉⢨⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠈⠻⣿⣿⣿⣿⣿⣿⣿⣥⣴⣦⣬⣿⣿⣿⣿⣿⣿⣿⠟⠁
⠀⠀⢸⣿⡿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⠿⢿⣿⡇⠀⠀
⠀⣠⣾⣿⠂⠀⠀⣤⣄⠀⠀⢰⣿⣿⣿⣿⡆⠐⣿⣷⣄⠀
⠀⣿⣿⡀⠀⠀⠈⠿⠟⠀⠀⠈⠻⣿⣿⡿⠃⠀⢀⣿⣿⠀
⠀⠘⠻⢿⣷⡀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⢀⣾⡿⠟⠃⠀
⠀⠀⠀⠸⣿⣿⣷⣦⣾⣿⣿⣿⣿⣦⣴⣾⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀
    """
    args = parser.parse_args()

    # Call the generate_passphrase function with the entered arguments.
    passphrase = generate_passphrase(args.words, args.symbols, args.numbers, args.delimiter)
    print(f'Generated passphrase: {passphrase}')

# This function creates the GUI for the passphrase generator.
def gui_interface():
    # This function generates a passphrase based on the user's input through the GUI.
    def generate():
        try:
            num_words = int(words_entry.get())
        except ValueError:
            num_words = 4
        add_symbols = symbols_var.get()
        add_numbers = numbers_var.get()
        delimiter = delimiter_entry.get()

        passphrase = generate_passphrase(num_words, add_symbols, add_numbers, delimiter)
        result_label.config(text=f'Generated passphrase: {passphrase}')

    # This function copies the generated passphrase to the clipboard.
    def copy_to_clipboard():
        root.clipboard_clear()
        clipboard_text = result_label.cget('text').replace('Generated passphrase: ', '')
        root.clipboard_append(clipboard_text)
        root.update()

    # Define the GUI elements.
    root = tk.Tk()
    root.title('Passphrase Generator')
    root.geometry("400x350")
    root.resizable(False, False)

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TLabel", font=("Segoe UI", 12))
    style.configure("TButton", font=("Segoe UI", 12))
    style.configure("TEntry", font=("Segoe UI", 12))

    mainframe = ttk.Frame(root, padding="20")
    mainframe.grid(row=0, column=0, sticky="NSEW")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text='Number of words:').grid(row=0, column=0, sticky="W", pady=(0,10))
    words_entry = ttk.Entry(mainframe, width=10)
    words_entry.insert(0, '4')
    words_entry.grid(row=0, column=1, sticky="EW", pady=(0,10))

    symbols_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(mainframe, text='Include symbols', variable=symbols_var).grid(row=1, column=0, columnspan=2, sticky="W", pady=(0,10))

    numbers_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(mainframe, text='Include numbers', variable=numbers_var).grid(row=2, column=0, columnspan=2, sticky="W", pady=(0,10))

    ttk.Label(mainframe, text='Delimiter:').grid(row=3, column=0, sticky="W", pady=(0,10))
    delimiter_entry = ttk.Entry(mainframe, width=10)
    delimiter_entry.insert(0, '-')
    delimiter_entry.grid(row=3, column=1, sticky="EW", pady=(0,10))

    generate_button = ttk.Button(mainframe, text='Generate', command=generate)
    generate_button.grid(row=4, column=0, columnspan=2, pady=(10,10))

    result_label = ttk.Label(mainframe, text='Generated passphrase:', wraplength=360)
    result_label.grid(row=5, column=0, columnspan=2, pady=(10,10))

    copy_button = ttk.Button(mainframe, text='Copy to Clipboard', command=copy_to_clipboard)
    copy_button.grid(row=6, column=0, columnspan=2, pady=(10,0))

    for i in range(2):
        mainframe.columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == '__main__':
    # Checks if the script is being run directly and calls the appropriate function.
    if len(sys.argv) > 1:
        cli_interface()
    else:
        gui_interface()
