import tkinter as tk

def set_message():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()
window.title('Welcome แอพของฉัน')
window.minsize(width=600, height=400)

title_label = tk.Label(master=window, text='Hello ทุกคน')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

button = tk.Button(master=window, text='OK', command=set_message)
button.pack()

window.mainloop()
