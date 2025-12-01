from tkinter import *

window = Tk()
window.geometry("600x400")


button = Button(
    text='кнопка 1',
    height=3,
    width=15
)

button.pack(pady=30)

window.mainloop()