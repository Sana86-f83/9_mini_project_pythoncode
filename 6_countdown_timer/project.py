import time
import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        total_seconds = int(entry.get())  
        countdown(total_seconds)  
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!") 

def countdown(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)  
        time_format = f"{mins:02d}:{secs:02d}"  
        label.config(text=time_format)  
        root.update()
        time.sleep(1)
        seconds -= 1

    label.config(text="00:00")  
    messagebox.showinfo("Time's Up!", "Countdown finished!")  

# GUI Setup
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("550x300")  
root.config(bg="black")

# Heading
heading = tk.Label(root, text="⏳ Countdown Timer", font=("Arial", 18, "bold"), fg="white", bg="black")
heading.pack(pady=10)

# Description
description = tk.Label(root, text="Enter time in seconds and start the countdown!", font=("Arial", 12), fg="white", bg="black")
description.pack()

# Timer Display (Centered)
label = tk.Label(root, text="00:00", font=("Arial", 40, "bold"), fg="red", bg="black")
label.pack(expand=True)  # Centers the timer

# Input Field
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=8)

# Start Button
button = tk.Button(root, text="Start Timer", font=("Arial", 14, "bold"), bg="green", fg="white", command=start_timer)
button.pack(pady=10)

root.mainloop()
