import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        temporary=f.read()
        temporary2=temporary.split(',')
        print (temporary2)


def robRzeczy():
    label=tk.Label(frame, text="ELOELOELO")
    label.pack()

canvas = tk.Canvas(root, height=700,width=700,bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button=tk.Button(root, text="Kliknij mnie bardzo plis",padx=20,pady=10,fg="white",bg="#123D42", command=robRzeczy)
button.pack()

button2=tk.Button(root, text="Kliknij mnie także",padx=35,pady=10,fg="white",bg="#122D42")
button2.pack()

root.mainloop()

with open('save.txt','w') as f: #generates file save.txt and set write
    f.write("treść"+',')
    f.write("WITAM")