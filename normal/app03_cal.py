import tkinter


def add(x):
    # เพิ่มเลข
    num_show: str
    num_show = text_label1['text'] + str(x)
    text_label1.configure(text=num_show)


def clr():
    text_label1.configure(text='')


window = tkinter.Tk()
window.option_add("*Font", "tahoma 20")
window.title('Calculator')
window.minsize(600, 400)

f1 = tkinter.Frame(window, bg="#4a4a4a")
f1.grid(row=0, column=0, columnspan=2)

f2 = tkinter.Frame(window, bg='#83f0ef')
f2.grid(row=1, column=0)

f3 = tkinter.Frame(window, bg='#e6ecb1')
f3.grid(row=1, column=1)

text_label1 = tkinter.Label(master=f1, text='เครื่องคิดเลข', height=2, width=42)
text_label1.grid(padx=10, pady=10)

bt1 = tkinter.Button(f2, text=1, height=1, width=8, command=lambda: add(1))
bt1.grid(row=0, column=0, padx=14, pady=10)

bt2 = tkinter.Button(f2, text=2, height=1, width=8, command=lambda: add(2))
bt2.grid(row=0, column=1, padx=14, pady=10)

bt3 = tkinter.Button(f2, text=3, height=1, width=8, command=lambda: add(3))
bt3.grid(row=0, column=2, padx=14, pady=10)

bt4 = tkinter.Button(f2, text=4, height=1, width=8, command=lambda: add(4))
bt4.grid(row=1, column=0, padx=14, pady=10)

bt5 = tkinter.Button(f2, text=5, height=1, width=8, command=lambda: add(5))
bt5.grid(row=1, column=1, padx=14, pady=10)

bt6 = tkinter.Button(f2, text=6, height=1, width=8, command=lambda: add(6))
bt6.grid(row=1, column=2, padx=14, pady=10)

bt7 = tkinter.Button(f2, text=7, height=1, width=8, command=lambda: add(7))
bt7.grid(row=2, column=0, padx=14, pady=10)

bt8 = tkinter.Button(f2, text=8, height=1, width=8, command=lambda: add(8))
bt8.grid(row=2, column=1, padx=14, pady=10)

bt9 = tkinter.Button(f2, text=9, height=1, width=8, command=lambda: add(9))
bt9.grid(row=2, column=2, padx=14, pady=10)

bt0 = tkinter.Button(f2, text=0, height=1, width=8, command=lambda: add(0))
bt0.grid(row=3, columnspan=3, padx=14, pady=2)

bt_cle = tkinter.Button(f3, text='C', width=10, command=clr)
bt_cle.grid(padx=10, pady=4)

bt_sub = tkinter.Button(f3, text='/', width=10)
bt_sub.grid(padx=10, pady=4)

bt_mul = tkinter.Button(f3, text='*', width=10)
bt_mul.grid(padx=10, pady=4)

bt_era = tkinter.Button(f3, text='-', width=10)
bt_era.grid(padx=10, pady=4)

bt_plu = tkinter.Button(f3, text='+', width=10)
bt_plu.grid(padx=10, pady=4)

bt_res = tkinter.Button(f3, text='=', width=10)
bt_res.grid(padx=10, pady=4)

window.mainloop()
