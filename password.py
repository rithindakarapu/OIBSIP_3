import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()
    exclude_chars = exclude_entry.get()
    
    if length <= 0:
        messagebox.showerror("Invalid input", "Password length must be a positive number.")
        return

    character_pool = ""
    if include_upper:
        character_pool += string.ascii_uppercase
    if include_lower:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    if exclude_chars:
        character_pool = ''.join([ch for ch in character_pool if ch not in exclude_chars])
    
    if not character_pool:
        messagebox.showerror("Invalid input", "No character types selected.")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Setup GUI
root = tk.Tk()
root.title("Advanced Password Generator")

# Length Label and Entry
tk.Label(root, text="Password Length").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Checkbuttons for character types
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).grid(row=1, column=0, columnspan=2)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).grid(row=2, column=0, columnspan=2)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=3, column=0, columnspan=2)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=4, column=0, columnspan=2)

# Exclude characters entry
tk.Label(root, text="Exclude Characters").grid(row=5, column=0)
exclude_entry = tk.Entry(root)
exclude_entry.grid(row=5, column=1)

# Password Entry and Buttons
password_entry = tk.Entry(root, width=50)
password_entry.grid(row=6, column=0, columnspan=2)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=7, column=0, columnspan=2)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=8, column=0, columnspan=2)

root.mainloop()
