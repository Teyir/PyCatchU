import customtkinter as ctk

from manager import db_manager
from utils import requests_pokemon


class TeamAddPage(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def setup(self):
        self.label_subtitle = ctk.CTkLabel(master=self,
                                           text="Ajouter une équipe",
                                           text_font=("Poppins", -25))  # font name and size in px

        self.label_subtitle.grid(row=0, column=1)

        self.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.rowconfigure(6, weight=0)
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.columnconfigure(7, weight=0)

        text_var = ctk.StringVar(value="Team Name")

        self.label = ctk.CTkLabel(master=self,
                                  textvariable=text_var,
                                  fg_color=self.fg_color)
        self.label.grid(row=1, column=3)

        self.input_name = ctk.CTkEntry(master=self)
        self.input_name.grid(row=2, column=3)

        self.poke_1 = ctk.CTkOptionMenu(master=self,
                                        values=self.get_pokemons_names())
        self.poke_1.grid(row=3, column=1)

        self.poke_2 = ctk.CTkOptionMenu(master=self,
                                        values=self.get_pokemons_names())
        self.poke_2.grid(row=3, column=2)

        self.poke_3 = ctk.CTkOptionMenu(master=self,
                                        values=self.get_pokemons_names())
        self.poke_3.grid(row=3, column=3)

        self.poke_4 = ctk.CTkOptionMenu(master=self,
                                        values=self.get_pokemons_names())
        self.poke_4.grid(row=3, column=4)

        self.poke_5 = ctk.CTkOptionMenu(master=self,
                                        values=self.get_pokemons_names())
        self.poke_5.grid(row=3, column=5)

        self.btn_submit = ctk.CTkButton(master=self,
                                        text='Envoyer',
                                        command=self.get_name)
        self.btn_submit.grid(row=4, column=3)

        print(self.input_name.get())

    def get_name(self):
        name = self.input_name.get()
        poke_1 = self.poke_1.get()
        poke_2 = self.poke_2.get()
        poke_3 = self.poke_3.get()
        poke_4 = self.poke_4.get()
        poke_5 = self.poke_5.get()

        conn = db_manager.DbManager().connection()

        db_manager.DbManager().add_team(conn=conn, name=name,
                                        pokemon_id_1=poke_1,
                                        pokemon_id_2=poke_2,
                                        pokemon_id_3=poke_3,
                                        pokemon_id_4=poke_4,
                                        pokemon_id_5=poke_5)
        self.master.frame_right.destroy()
        from pages.team_page import TeamPage
        self.master.frame_right = TeamPage()
        self.master.frame_right.setup()

    def get_pokemons_names(self):
        toReturn = []
        for pokemon in requests_pokemon.get_pokemons()['results']:
            toReturn += [pokemon['name']]
        return toReturn
