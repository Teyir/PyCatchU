import tkinter

import customtkinter


class HomePage(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def setup(self):
        img = tkinter.PhotoImage(file="./assets/logo.png")

        self.button_3 = customtkinter.CTkButton(master=self,
                                                image=img, text="", fg_color=self.fg_color, hover=False)
        self.button_3.grid(row=2, column=1, pady=10, padx=20)

        self.label_subtitle = customtkinter.CTkLabel(master=self,
                                                     text="Made with 🍆 by Thomas.T / Thomas.Gry / Axel.B / Valentin.B",
                                                     text_font=("Poppins", -16))  # font name and size in px

        self.label_subtitle.grid(row=3, column=1, pady=0, padx=0)
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.rowconfigure(6, weight=0)
        self.columnconfigure((0, 1, 3), weight=1)
        self.columnconfigure(2, weight=0)