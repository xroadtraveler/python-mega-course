from tkinter import *

window = Tk()

def kg_to_grams():
    # print(e1_value.get()) # for testing
    grams = float(e1_value.get()) * 1000
    t1.delete("1.0", END)
    t1.insert(END, grams)

def kg_to_pounds():
    # print(e1_value.get()) # for testing
    pounds = float(e1_value.get()) * 2.20462
    t2.delete("1.0", END)
    t2.insert(END, pounds)

def kg_to_ounces():
    # print(e1_value.get()) # for testing
    ounces = float(e1_value.get()) * 35.274
    t3.delete("1.0", END)
    t3.insert(END, ounces)

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

b1 = Button(window, text="Convert", command=lambda: [kg_to_grams(), kg_to_pounds(), kg_to_ounces()])
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
