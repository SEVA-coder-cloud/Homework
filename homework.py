from tkinter import *


window = Tk()
window.geometry("600x400")
window.title("Вправа 4.2")


def click():
    button['text'] = 'A класу'
    button['height'] = 2
    button['width'] = 30
    button['fg'] = 'red'
    button['state'] = 'disable'   


button = Button(
    text='кнопка 1',
    height=3,
    width=15,
    command=click
)


button.pack(pady=30)


window.mainloop()