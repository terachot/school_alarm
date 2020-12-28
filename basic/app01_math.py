import tkinter as tk


def cal():
    number = int(text_box.get())
    text = ''
    for i in range(1, 13):
        text += str(i) + ' x ' + str(number) + ' = ' + str(i * number) + '\n'
    text_label2.configure(text=text)


window = tk.Tk()
window.title('Calculator')
window.minsize(600, 400)

text_label1 = tk.Label(master=window, text='สูตรคูณ')
text_label1.pack(pady=10)

text_box = tk.Entry(master=window, width=20)
text_box.pack()

button = tk.Button(master=window, text='คำนวณ', width=15, height = 2, command=cal)
button.pack(pady=10)

text_label2 = tk.Label(master=window)
text_label2.pack()

window.mainloop()
