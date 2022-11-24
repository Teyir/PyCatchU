from functools import partial

import customtkinter as ctk

from manager import db_manager, local_storage
from pages.all_pokemon_page import AllPokemonPage
from utils import requests_pokemon


class TeamAddPage(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.poke_1 = None
        self.poke_2 = None
        self.poke_3 = None
        self.poke_4 = None
        self.poke_5 = None
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def setup(self):
        self.master.label_subtitle = ctk.CTkLabel(master=self,
                                                  text="Ajouter une équipe",
                                                  text_font=("Poppins", -25))  # font name and size in px

        self.master.label_subtitle.grid(row=0, column=1)

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

        if not local_storage.LocalStorage().get_data(item=1):
            self.master.poke_1 = ctk.CTkButton(master=self, text='+', command=partial(self.add_pokemon, 1))
        else:
            self.master.poke_1 = ctk.CTkButton(master=self, text=local_storage.LocalStorage().get_data(item=1))
            self.poke_1 = local_storage.LocalStorage().get_data(item=1)
        self.master.poke_1.grid(row=3, column=1)

        if not local_storage.LocalStorage().get_data(item=2):
            self.master.poke_2 = ctk.CTkButton(master=self, text='+', command=partial(self.add_pokemon, 2))
        else:
            self.master.poke_2 = ctk.CTkButton(master=self, text=local_storage.LocalStorage().get_data(item=2))
            self.poke_2 = local_storage.LocalStorage().get_data(item=2)
        self.master.poke_2.grid(row=3, column=2)

        if not local_storage.LocalStorage().get_data(item=3):
            self.master.poke_3 = ctk.CTkButton(master=self, text='+', command=partial(self.add_pokemon, 3))
        else:
            self.master.poke_3 = ctk.CTkButton(master=self, text=local_storage.LocalStorage().get_data(item=3))
            self.poke_3 = local_storage.LocalStorage().get_data(item=3)
        self.master.poke_3.grid(row=3, column=3)

        if not local_storage.LocalStorage().get_data(item=4):
            self.master.poke_4 = ctk.CTkButton(master=self, text='+', command=partial(self.add_pokemon, 4))
        else:
            self.master.poke_4 = ctk.CTkButton(master=self, text=local_storage.LocalStorage().get_data(item=4))
            self.poke_4 = local_storage.LocalStorage().get_data(item=4)
        self.master.poke_4.grid(row=3, column=4)

        if not local_storage.LocalStorage().get_data(item=5):
            self.master.poke_5 = ctk.CTkButton(master=self, text='+', command=partial(self.add_pokemon, 5))
        else:
            self.master.poke_5 = ctk.CTkButton(master=self, text=local_storage.LocalStorage().get_data(item=5))
            self.poke_5 = local_storage.LocalStorage().get_data(item=5)
        self.master.poke_5.grid(row=3, column=5)

        if self.poke_1 is not None and self.poke_2 is not None and self.poke_3 is not None and self.poke_4 is not None and self.poke_5 is not None:
            self.master.btn_submit = ctk.CTkButton(master=self,
                                                   text='Envoyer',
                                                   command=self.get_name)
            self.master.btn_submit.grid(row=4, column=3)

        print(self.master.input_name.get())

    def add_pokemon(self, pokemon):
        self.master.frame_right.destroy()
        self.master.frame_right = AllPokemonPage(edit=True, pokemon_number=pokemon)
        self.master.frame_right.setup()

    def get_name(self):
        name = self.master.input_name.get()
        poke_1 = self.poke_1
        poke_2 = self.poke_2
        poke_3 = self.poke_3
        poke_4 = self.poke_4
        poke_5 = self.poke_5

        # If name input is empty, we stop the function
        if not name:
            return

        conn = db_manager.DbManager().connection()

        db_manager.DbManager().add_team(conn=conn, name=name,
                                        pokemon_id_1=poke_1,
                                        pokemon_id_2=poke_2,
                                        pokemon_id_3=poke_3,
                                        pokemon_id_4=poke_4,
                                        pokemon_id_5=poke_5)

        local_storage.LocalStorage().clear_data()

        self.master.frame_right.destroy()
        from pages.team_page import TeamPage
        self.master.frame_right = TeamPage()
        self.master.frame_right.setup()

    def get_pokemons_names(self):
        to_return = []
        for pokemon in requests_pokemon.get_pokemons()['results']:
            to_return += [pokemon['name']]
        return to_return
