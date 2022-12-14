import tkinter
from functools import partial
from tkinter import ttk

import customtkinter

from manager import db_manager
from pages.team_add_page import TeamAddPage
from utils import requests_pokemon


class TeamPage(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.conn = db_manager.DbManager().connection()

    def setup(self):
        teams = db_manager.DbManager().fetch_teams(self.conn)
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

            i = 2
            array_poke_img = []
            while i <= 6:
                array_poke_img.append(requests_pokemon.get_pokemon_sprite(team[i]).subsample(2))
                i += 1

            frame_team = customtkinter.CTkFrame(master=self,
                                                width=200,
                                                height=50,
                                                corner_radius=15,
                                                fg_color=self.bg_color,
                                                border_width=1,
                                                border_color="white")
            frame_team.grid(row=row_value, column=column_value, sticky="nsew", padx=20, pady=10)

            frame_team.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
            frame_team.rowconfigure(7, weight=0)
            frame_team.columnconfigure((0, 1, 3), weight=1)
            frame_team.columnconfigure(2, weight=0)

            label_team = customtkinter.CTkLabel(text=team[1], master=frame_team)
            label_team.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

            self.button_del_team = customtkinter.CTkButton(master=frame_team,
                                                           text="Supprimer",
                                                           border_width=1,
                                                           text_color="red",
                                                           fg_color=self.fg_color,
                                                           hover_color=self.bg_color,
                                                           border_color="red",
                                                           command=partial(self.button_team_del, team_name=team[1]))
            self.button_del_team.grid(row=1, column=2, padx=(150, 0))

            image_frame = customtkinter.CTkFrame(master=frame_team,
                                                 width=200,
                                                 height=50,
                                                 corner_radius=15,
                                                 fg_color=self.bg_color,
                                                 border_width=1,
                                                 border_color="white")
            image_frame.grid(row=4, column=2, sticky="nsew", padx=(0, 20))

            image_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
            image_frame.rowconfigure(5, weight=0)
            image_frame.columnconfigure((0, 1, 3), weight=1)
            image_frame.columnconfigure(3, weight=0)

            x = 0
            while x < len(array_poke_img):
                self.image = customtkinter.CTkButton(master=image_frame, image=array_poke_img[x], text="",
                                                     fg_color=self.bg_color, width=10, padx=0,
                                                     hover=False)
                self.image.grid(row=2, column=x, sticky="w", padx=5)
                x += 1

            if column_value == 0:
                column_value = 3
            else:
                column_value = 0
            if row_count == 2 or row_count == 4:
                row_value += 1

            if len(teams) == 1:  # Oblig?? de mettre une frame avec les m??mes ??l??ments pour ne pas avoir de d??s??quilibre dans l'UI
                frame_team = customtkinter.CTkFrame(master=self,
                                                    width=200,
                                                    height=50,
                                                    corner_radius=10,
                                                    fg_color=self.fg_color)
                frame_team.grid(row=row_value, column=column_value, sticky="nsew", padx=20, pady=10)

                label_team = customtkinter.CTkLabel(text='---', master=frame_team, text_color=self.fg_color)
                label_team.grid(row=row_value, column=column_value, sticky="nsew")

                self.button_del_team = customtkinter.CTkButton(master=frame_team,
                                                               text="---",
                                                               fg_color=self.fg_color,
                                                               text_color=self.fg_color,
                                                               hover=False)
                self.button_del_team.grid(row=1, column=2)
                image_frame = customtkinter.CTkFrame(master=frame_team,
                                                     width=200,
                                                     height=50,
                                                     corner_radius=15,
                                                     fg_color=self.fg_color,
                                                     border_width=1)
                image_frame.grid(row=4, column=2, sticky="nsew", padx=(0, 20))

                image_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
                image_frame.rowconfigure(5, weight=0)
                image_frame.columnconfigure((0, 1, 3), weight=1)
                image_frame.columnconfigure(3, weight=0)
                y = 0
                while y < 5:
                    self.image = customtkinter.CTkButton(master=image_frame, text="---", text_color=self.fg_color,
                                                         fg_color=self.fg_color, width=10, padx=0,
                                                         hover=False)
                    self.image.grid(row=2, column=y, sticky="w", padx=5)
                    y += 1
            if row_value >= 6:
                break

        if not teams:
            frame_team = customtkinter.CTkFrame(master=self,
                                                width=200,
                                                height=50,
                                                corner_radius=10,
                                                fg_color=self.bg_color,
                                                border_width=1,
                                                border_color="white")
            frame_team.grid(row=2, column=1, sticky="nsew", padx=20, pady=10)

            frame_team.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
            frame_team.rowconfigure(6, weight=0)
            frame_team.columnconfigure((0, 1, 3), weight=1)
            frame_team.columnconfigure(2, weight=0)

            label_team = customtkinter.CTkLabel(text="Tu n'a pas encore d'??quipes de cr??es", master=frame_team)
            label_team.grid(row=2, column=1, sticky="nsew")

        self.button_add_team = customtkinter.CTkButton(master=self,
                                                       text="Ajouter une ??quipe",
                                                       command=self.button_team_add)
        self.button_add_team.grid(row=5, column=1)

    def button_team_add(self):
        self.master.frame_right.destroy()
        self.master.frame_right = TeamAddPage()
        self.master.frame_right.setup()

    def button_team_del(self, team_name):
        dialog = customtkinter.CTkInputDialog(text="??crivez le nom de l'??quipe pour confirmer",
                                              title="Suppression de " + team_name)
        if team_name == dialog.get_input():
            db_manager.DbManager().delete_team(self.conn, team_name)
            self.master.frame_right.destroy()
            self.master.frame_right = TeamPage()
            self.master.frame_right.setup()
        elif team_name != dialog.get_input():
            self.button_team_del(team_name)
