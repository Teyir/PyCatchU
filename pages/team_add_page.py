from functools import partial

import customtkinter as ctk

from manager import db_manager, local_storage
from pages.all_pokemon_page import AllPokemonPage
from utils import requests_pokemon


class TeamAddPage(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.poke = {}
        self.poke_1 = None
        self.poke_2 = None
        self.poke_3 = None
        self.poke_4 = None
        self.poke_5 = None
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def setup(self):

        # Refresh button
        self.master.refresh = ctk.CTkButton(master=self, text="🔄", command=self.clear)
        self.master.refresh.grid(row=1, column=0)

        self.master.label_subtitle = ctk.CTkLabel(master=self,
                                                  text="Ajouter une équipe",
                                                  text_font=("Poppins", -25))  # font name and size in px

        self.master.label_subtitle.grid(row=0, column=0)

        self.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.rowconfigure(6, weight=0)
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.columnconfigure(7, weight=0)

        text_var = ctk.StringVar(value="Nom de votre équipe")

        self.master.label = ctk.CTkLabel(master=self,
                                         textvariable=text_var,
                                         fg_color=self.fg_color)
        self.master.label.grid(row=1, column=3)

        self.master.input_name = ctk.CTkEntry(master=self)
        self.master.input_name.grid(row=2, column=3)

        i = 1
        while i <= 5:
            if not local_storage.LocalStorage().get_data(item=i):
                self.master.poke = ctk.CTkButton(master=self, text='+', command=partial(self.add_pokemon, i))
            else:
                self.master.poke = ctk.CTkButton(master=self, text=local_storage.LocalStorage().get_data(item=i))
                self.poke[i] = local_storage.LocalStorage().get_data(item=i)
            self.master.poke.grid(row=3, column=i)
            i += 1

        if 5 == len(self.poke):
            self.master.btn_submit = ctk.CTkButton(master=self,
                                                   text='Envoyer',
                                                   command=self.get_name)
            self.master.btn_submit.grid(row=4, column=3)

    def add_pokemon(self, pokemon):
        self.master.frame_right.destroy()
        self.master.frame_right = AllPokemonPage(edit=True, pokemon_number=pokemon)
        self.master.frame_right.setup()

    def get_name(self):
        name = self.master.input_name.get()

        # If name input is empty, we stop the function
        if not name:
            return

        conn = db_manager.DbManager().connection()

        db_manager.DbManager().add_team(conn=conn, name=name,
                                        pokemon_id_1=self.poke[1],
                                        pokemon_id_2=self.poke[2],
                                        pokemon_id_3=self.poke[3],
                                        pokemon_id_4=self.poke[4],
                                        pokemon_id_5=self.poke[5])

        local_storage.LocalStorage().clear_data()

        self.master.frame_right.destroy()
        from pages.team_page import TeamPage
        self.master.frame_right = TeamPage()
        self.master.frame_right.setup()

    def clear(self):
        local_storage.LocalStorage().clear_data()

        self.master.frame_right.destroy()
        self.master.frame_right = TeamAddPage()
        self.master.frame_right.setup()

    def get_pokemons_names(self):
        to_return = []
        for pokemon in requests_pokemon.get_pokemons()['results']:
            to_return += [pokemon['name']]
        return to_return
