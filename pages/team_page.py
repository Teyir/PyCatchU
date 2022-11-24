import tkinter
from tkinter import ttk

import customtkinter

from manager import db_manager
from pages.team_add_page import TeamAddPage


class TeamPage(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def setup(self):
        conn = db_manager.DbManager().connection()
        teams = db_manager.DbManager().fetch_teams(conn)
        self.label_subtitle = customtkinter.CTkLabel(master=self,
                                                     text="Equipes",
                                                     text_font=("Poppins", -25))  # font name and size in px

        self.label_subtitle.grid(row=0, column=1)

        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.rowconfigure(6, weight=0)
        self.columnconfigure((0, 1, 3), weight=1)
        self.columnconfigure(2, weight=0)

        row_value = 1
        column_value = 0
        row_count = 0
        for team in teams:
            row_count += 1
            frame_team = customtkinter.CTkFrame(master=self,
                                                width=200,
                                                height=50,
                                                corner_radius=10,
                                                fg_color=self.bg_color)
            frame_team.grid(row=row_value, column=column_value, sticky="nsew", padx=20, pady=10)
            frame_team.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
            frame_team.rowconfigure(6, weight=0)
            frame_team.columnconfigure((0, 1, 3), weight=1)
            frame_team.columnconfigure(2, weight=0)
            label_team = customtkinter.CTkLabel(text=team[1], master=frame_team)
            label_team.grid(row=1, column=1, sticky="nsew")
            if column_value == 0:
                column_value = 3
            else:
                column_value = 0
            if row_count == 2:
                row_value += 1
            if len(teams) == 1:
                frame_team = customtkinter.CTkFrame(master=self,
                                                    width=200,
                                                    height=50,
                                                    corner_radius=10,
                                                    fg_color=self.fg_color)
                frame_team.grid(row=row_value, column=column_value, sticky="nsew", padx=20, pady=10)
                label_team = customtkinter.CTkLabel(text='---', master=frame_team, text_color=self.fg_color)
                label_team.grid(row=row_value, column=column_value, sticky="nsew")
            if row_value == 4:
                break

        if not teams:
            frame_team = customtkinter.CTkFrame(master=self,
                                                width=200,
                                                height=50,
                                                corner_radius=10,
                                                fg_color=self.bg_color)
            frame_team.grid(row=2, column=1, sticky="nsew", padx=20, pady=10)
            frame_team.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
            frame_team.rowconfigure(6, weight=0)
            frame_team.columnconfigure((0, 1, 3), weight=1)
            frame_team.columnconfigure(2, weight=0)
            label_team = customtkinter.CTkLabel(text="Tu n'a pas encore d'équipes de crées", master=frame_team)
            label_team.grid(row=2, column=1, sticky="nsew")

        self.button_add_team = customtkinter.CTkButton(master=self,
                                                       text="Ajouter une équipe",
                                                       command=self.button_team_add)
        self.button_add_team.grid(row=5, column=1)

    def button_team_add(self):
        self.master.frame_right.destroy()
        self.master.frame_right = TeamAddPage()
        self.master.frame_right.setup()
