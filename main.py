import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=700,width=700,bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button=tk.Button(root, text="Kliknij mnie",padx=25,pady=10,fg="white",bg="#123D42")
button.pack()

root.mainloop()
