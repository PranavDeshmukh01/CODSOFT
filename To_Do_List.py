import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox.delete(0, tk.END)
 
root = tk.Tk()
root.title("To-Do List")

 
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)

 
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=10)

clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
clear_button.grid(row=0, column=3, padx=5, pady=10)

 
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

 
root.mainloop()
