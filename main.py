from tkinter import *
window = Tk()
window.title("welcome to Like geeks ")
window. geometry('350x200')
lbl = Label(window, text="hello world")
lbl = Label(window, text="hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
btn = Button(window, text="Click Me")

btn.grid(column=1,row=0)

btn = Button(window, text="Click me", bg="orange",fg="red")


def clicked():
    lbl.configure(text="Button was clicked!!")

btn = Button(window, text="click me", command=clicked)
btn.grid(column=1, row=0)






window.mainloop()

