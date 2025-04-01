import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%I:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1 second

# GUI Setup
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")

label = tk.Label(root, font=("Arial", 40), bg="black", fg="white")
label.pack(expand=True)

update_time()

root.mainloop()