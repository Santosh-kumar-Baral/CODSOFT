
import tkinter as tk

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            # Evaluate the expression and update the display
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        # Clear the screen
        screen.set("")
    else:
        # Append the clicked button's text to the screen
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")

# Create a variable to store the expression
screen = tk.StringVar()

# Entry widget to display the expression
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10, expand=True)

# Create a frame for the buttons
frame = tk.Frame(root)
frame.pack()

# Buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
]

row, col = 0, 0
for text in button_texts:
    button = tk.Button(frame, text=text, font="lucida 15", padx=20, pady=20)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()





