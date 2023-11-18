import tkinter as tk
import pyperclip

# Specify the file path and name
file_path = 'clipboard_contents.txt'

# Function to write clipboard contents to file
def write_to_file():
    clipboard_content = pyperclip.paste()

    # Append the clipboard contents to the file
    with open(file_path, 'a') as file:
        file.write(clipboard_content + "\n")

    print(f"Clipboard contents appended to '{file_path}'")

# Create a function to check for clipboard changes
def check_clipboard():
    current_clipboard_content = pyperclip.paste()
    if current_clipboard_content != check_clipboard.last_clipboard_content:
        check_clipboard.last_clipboard_content = current_clipboard_content
        write_to_file()
    root.after(200, check_clipboard)

check_clipboard.last_clipboard_content = pyperclip.paste()

# Create the main window
root = tk.Tk()
root.withdraw()

# Start checking for clipboard changes
check_clipboard()

# Start the main GUI loop
root.mainloop()