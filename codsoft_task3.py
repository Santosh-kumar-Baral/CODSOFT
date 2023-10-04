import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_var.get())
    character_set = ""

    if include_lowercase.get():
        character_set += string.ascii_lowercase
    if include_uppercase.get():
        character_set += string.ascii_uppercase
    if include_digits.get():
        character_set += string.digits
    if include_special_chars.get():
        character_set += string.punctuation

    if character_set:
        password = ''.join(random.choice(character_set) for _ in range(password_length))
        password_var.set(password)
    else:
        password_var.set("Please select at least one character set")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

title_label = tk.Label(frame, text="Password Generator", font=("Helvetica", 16))
title_label.grid(row=0, columnspan=2, pady=10)

length_label = tk.Label(frame, text="Password Length:", font=("Helvetica", 12))
length_label.grid(row=1, column=0, padx=10)

length_var = tk.StringVar()
length_entry = tk.Entry(frame, textvariable=length_var, font=("Helvetica", 12), width=5)
length_entry.grid(row=1, column=1)

include_lowercase = tk.BooleanVar()
include_uppercase = tk.BooleanVar()
include_digits = tk.BooleanVar()
include_special_chars = tk.BooleanVar()

lowercase_check = tk.Checkbutton(frame, text="Lowercase", variable=include_lowercase, font=("Helvetica", 12))
uppercase_check = tk.Checkbutton(frame, text="Uppercase", variable=include_uppercase, font=("Helvetica", 12))
digits_check = tk.Checkbutton(frame, text="Digits", variable=include_digits, font=("Helvetica", 12))
special_chars_check = tk.Checkbutton(frame, text="Special Characters", variable=include_special_chars, font=("Helvetica", 12))

lowercase_check.grid(row=2, column=0, padx=10, sticky="w")
uppercase_check.grid(row=3, column=0, padx=10, sticky="w")
digits_check.grid(row=4, column=0, padx=10, sticky="w")
special_chars_check.grid(row=5, column=0, padx=10, sticky="w")

generate_button = tk.Button(frame, text="Generate Password", command=generate_password, font=("Helvetica", 12))
generate_button.grid(row=6, columnspan=2, pady=10)

password_var = tk.StringVar()
password_label = tk.Label(frame, textvariable=password_var, font=("Helvetica", 14), wraplength=250)
password_label.grid(row=7, columnspan=2, pady=10)

root.mainloop()
