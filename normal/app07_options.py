import tkinter as tk

window = tk.Tk()
window.minsize(400, 300)

name = "Welcome to Computer Class Room"

label1 = tk.Label(window, text=name)
label1.configure(font='consolas 14')
label1.pack(padx=10, pady=10)

# padx pady ระยะขอบนอก ipadx ipady ระยะขอบใน

textbox1 = tk.Entry(window)
textbox1.configure(font='tahoma 12')
textbox1.pack(padx=10, pady=5, ipadx=20, ipady=3)

button1 = tk.Button(window, text='ตกลง')
button1.configure(font='tahoma 12')
button1.pack(padx=10, pady=5, ipadx=60, ipady=3)

label2 = tk.Label(window, text='')
label2.configure(font='consolas 14')
label2.pack(padx=10, pady=5)

window.mainloop()
