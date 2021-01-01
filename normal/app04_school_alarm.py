from tkinter import *
from tkinter import ttk
import tkinter as tk

windows1 = tk.Tk()
windows1.title('School Alarm')
screen_width = windows1.winfo_screenwidth()
screen_height = windows1.winfo_screenheight()
windows1.minsize(int(screen_width * 50 / 100), int(screen_height * 80 / 100))
windows1.option_add("*Font", "Pridi 20")

text_label1 = tk.Label(master=windows1, bg="#4a4a4a", fg="#fefefe", text='โปรแกรมตั้งเวลาเตือนโรงเรียน')
text_label1.config(font=("Courier", 44))
text_label1.pack(fill=X, padx=10, pady=5)

text_label2 = tk.Label(master=windows1, text='เวลาปัจจุบัน')
text_label2.pack(padx=10, pady=5)

tree = ttk.Treeview(master=windows1)
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

windows1.mainloop()
