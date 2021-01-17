from tkinter import *

root = Tk()
root.minsize(300, 200)

height = 5
width = 5
for i in range(height):  # Rows
    for j in range(width):  # Columns
        b = Label(root, text="test",height=4, width=8, bg="#bbbbbb", fg="#333333")
        b.grid(row=i, column=j, padx=2, pady=2)

mainloop()
