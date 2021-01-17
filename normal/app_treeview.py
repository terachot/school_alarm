from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.minsize(400, 300)

tree = ttk.Treeview(master=root)
tree["columns"] = ("one", "two", "three")

tree.column("#0", width=80, minwidth=80, stretch=tk.NO)
tree.column("one", width=200, minwidth=200, stretch=tk.NO)
tree.column("two", width=300, minwidth=300)
tree.column("three", width=150, minwidth=150, stretch=tk.NO)

tree.heading('#0', text='#', anchor=tk.W)
tree.heading('one', text='Time', anchor=tk.W)
tree.heading('two', text='Sound', anchor=tk.W)
tree.heading('three', text='Active', anchor=tk.W)

tree.insert(parent='', index='end', iid=0, text="01", values=("08:20", "kap1", "enable"))
tree.insert(parent='', index='end', iid=1, text="02", values=("09:10", "kap2", "enable"))
tree.pack(padx=10, fill=tk.X)

root.mainloop()