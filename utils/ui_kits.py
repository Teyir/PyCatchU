import customtkinter as ctk


def img(master, image):
    return ctk.CTkButton(master=master, image=image, text="", fg_color=master.fg_color, hover=False)

