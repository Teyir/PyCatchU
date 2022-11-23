import tkinter
from tkinter import ttk

import customtkinter


class TeamPage(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def setup(self):
        self.label_subtitle = customtkinter.CTkLabel(master=self,
                                                     text="Equipes",
                                                     text_font=("Poppins", -25))  # font name and size in px

        self.label_subtitle.grid(row=0, column=1)

        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.rowconfigure(6, weight=0)
        self.columnconfigure((0, 1, 3), weight=1)
        self.columnconfigure(2, weight=0)

        frame_team = customtkinter.CTkFrame(master=self,
                                       width=200,
                                       height=50,
                                       corner_radius=10,
                                        fg_color='blue')
        frame_team.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        frame_team = customtkinter.CTkFrame(master=self,
                                            width=200,
                                            height=50,
                                            corner_radius=10,
                                            fg_color='yellow')
        frame_team.grid(row=1, column=3, sticky="nsew", padx=20, pady=10)

        frame_team = customtkinter.CTkFrame(master=self,
                                            width=200,
                                            height=50,
                                            corner_radius=10,
                                            fg_color='green')
        frame_team.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

        frame_team = customtkinter.CTkFrame(master=self,
                                            width=200,
                                            height=50,
                                            corner_radius=10,
                                            fg_color='purple')
        frame_team.grid(row=2, column=3, sticky="nsew", padx=20, pady=10)

        frame_team = customtkinter.CTkFrame(master=self,
                                            width=200,
                                            height=50,
                                            corner_radius=10,
                                            fg_color='red')
        frame_team.grid(row=3, column=0, sticky="nsew", padx=20, pady=10)

        frame_team = customtkinter.CTkFrame(master=self,
                                            width=200,
                                            height=50,
                                            corner_radius=10,
                                            fg_color='brown')
        frame_team.grid(row=3, column=3, sticky="nsew", padx=20, pady=10)
