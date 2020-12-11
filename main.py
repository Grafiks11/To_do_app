import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
task = []

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        temporary=f.read()
        temporary2=temporary.split(',')
        print (temporary2)


def addTask():
    for widget in frame.winfo_children(): #delete previous version of frame
        widget.destroy()
    task.append(textBox.get("1.0",'end-1c')) #reads text from textBox
    for i in range(len(task)):
        label=tk.Label(frame, text=task[i])
        label.pack()

canvas = tk.Canvas(root, height=700,width=700,bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="grey")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.2)

textBox=tk.Text(root, height=5, width=15)
textBox.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.1)

addTaskButton=tk.Button(root, text="Dodaj zadanie",padx=20,pady=10,fg="white",bg="#123D42", command=addTask)
addTaskButton.pack()

button2=tk.Button(root, text="Kliknij mnie także",padx=35,pady=10,fg="white",bg="#122D42")
button2.pack()

root.mainloop()

with open('save.txt','w') as f: #generates file save.txt and set write
    for tasks in task:
        f.write(tasks + ',')
