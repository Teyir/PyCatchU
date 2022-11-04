# Ici on dev la page ou il y a aura les 151 premiers pokémons (Call API t'as compris)
from tkinter import *
from tkinter import ttk

def draw(window = Tk()):
    window.title('PyCatchU | All')
    window.geometry('1100x1020')
    window.resizable(width=False, height=False)
    window.configure(bg="#444466")

    ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

    main_frame = Frame(window, width=540, height=305, bg="#444466")
    main_frame.grid(row=0, column=0, padx=1, pady=1)

    window.mainloop()