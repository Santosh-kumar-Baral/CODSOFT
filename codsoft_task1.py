# import tkinter as tk
# from tkinter import messagebox

# def add_task():
#     task = entry.get()
#     if task:
#         task_listbox.insert(tk.END, task)
#         entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("Warning", "Please enter a task!")

# def remove_task():
#     try:
#         selected_task = task_listbox.curselection()[0]
#         task_listbox.delete(selected_task)
#     except IndexError:
#         pass

# def clear_list():
#     task_listbox.delete(0, tk.END)

# # Create the main window
# root = tk.Tk()
# root.title("To-Do List")

# # Create and configure the task entry field with a placeholder
# entry = tk.Entry(root, width=30, font=("Helvetica", 14))
# entry.insert(0, "Enter a task...")
# entry.bind("<FocusIn>", lambda event: entry.delete(0, tk.END))  # Clear the placeholder text on focus
# entry.pack(pady=10)

# # Create and configure the task listbox with a scroll bar
# task_listbox = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12))
# task_listbox.pack()

# # Create buttons for adding, removing, and clearing tasks with custom colors and padding
# button_frame = tk.Frame(root)
# button_frame.pack(pady=10)

# add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10)
# remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, bg="#f44336", fg="white", font=("Helvetica", 12), padx=10)
# clear_button = tk.Button(button_frame, text="Clear All", command=clear_list, bg="#2196F3", fg="white", font=("Helvetica", 12), padx=10)

# add_button.grid(row=0, column=0)
# remove_button.grid(row=0, column=1)
# clear_button.grid(row=0, column=2)

# # Start the tkinter main loop
# root.mainloop()




# import tkinter as tk

# def add_task():
#     task = task_entry.get()
#     if task:
#         task_list.insert(tk.END, task)
#         task_entry.delete(0, tk.END)

# def remove_task():
#     try:
#         selected_task_index = task_list.curselection()[0]
#         task_list.delete(selected_task_index)
#     except IndexError:
#         pass

# # Create the main window
# root = tk.Tk()
# root.title("To-Do List")

# # Entry for adding tasks
# task_entry = tk.Entry(root, font=("Helvetica", 14))
# task_entry.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# # Buttons for adding and removing tasks
# add_button = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12))
# remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Helvetica", 12))
# add_button.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)
# remove_button.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

# # Listbox for displaying tasks
# task_list = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12))
# task_list.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# # Run the Tkinter main loop
# root.mainloop()



# new
import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to remove a task
def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

# Function to clear all tasks
def clear_all_tasks():
    confirmed = messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?")
    if confirmed:
        task_list.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Colors and styles
bg_color = "#F0F0F0"
button_color = "#4CAF50"
button_hover_color = "#45a049"
font_color = "#333333"

root.configure(bg=bg_color)

# Entry for adding tasks
task_entry = tk.Entry(root, font=("Helvetica", 14))
task_entry.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Frame for buttons
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

# Buttons for adding, removing, and clearing tasks
add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Helvetica", 12), bg=button_color, fg=font_color, activebackground=button_hover_color)
remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, font=("Helvetica", 12), bg=button_color, fg=font_color, activebackground=button_hover_color)
clear_all_button = tk.Button(button_frame, text="Clear All", command=clear_all_tasks, font=("Helvetica", 12), bg=button_color, fg=font_color, activebackground=button_hover_color)

add_button.grid(row=0, column=0, padx=5)
remove_button.grid(row=0, column=1, padx=5)
clear_all_button.grid(row=0, column=2, padx=5)

# Listbox for displaying tasks
task_list = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12), bg=bg_color, selectbackground=button_hover_color)
task_list.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Run the Tkinter main loop
root.mainloop()



