from functools import partial
from tkinter import font

import customtkinter as ctk
import re

from manager import local_storage
from models.pokemon_model import Pokemon
from pages.home_page import HomePage
from pages.pokemon import PokemonPage
from utils.requests_pokemon import get_all_pokemon, getPixelSprite


class AllPokemonPage(ctk.CTkFrame):

    def __init__(self, edit=False, pokemon_number=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.edit = edit
        self.pokemon_number = pokemon_number
        self.n_page = 1

    def setup(self):

        self.columnconfigure((0, 2), weight=1)
        self.columnconfigure(1, weight=10)
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=10)

        self.button_next = ctk.CTkButton(master=self, width=30, height=30, text=">", command=self.nextPage)
        self.button_next.grid(column=2, row=2)

        self.button_prev = ctk.CTkButton(master=self, width=30, height=30, text="<", command=self.prevPage)
        self.button_prev.grid(column=0, row=2)

        self.drawPage(self.n_page)

    def nextPage(self):
        self.n_page += 1
        self.drawPage(self.n_page)

    def prevPage(self):
        if self.n_page != 1:
            self.n_page = 0 if self.n_page - 1 < 0 else self.n_page - 1
            self.drawPage(self.n_page)

    def drawPage(self, page=None):
        if hasattr(self, 'pokeList'):
            self.pokeList.destroy()

        if page is None:
            page = self.n_page

        self.pokeList = ctk.CTkFrame(master=self)
        self.pokeList.grid(column=0, columnspan=3, row=1, sticky="nswe")
        self.pokeList.columnconfigure((0, 1, 2, 3), weight=1)
        self.pokeList.rowconfigure((0, 1, 2), weight=1)

        self.searchbar = ctk.CTkEntry(master=self, height=16, width=1000)
        self.searchbar.grid(row=0, column=1)

        self.buttonSearch = ctk.CTkButton(master=self, command=self.search, text='🔍')
        self.buttonSearch.grid(row=0, column=2)

        self.pokeList.item = {}

        i = 0

        requests = get_all_pokemon(page=page, lenght=12)

        for pokemon in requests.keys():
            self.pokeList.item[requests[pokemon]] = PokeCard(pokemon, requests[pokemon], master=self.pokeList,
                                                             edit=self.edit, pokemon_number=self.pokemon_number)
            self.pokeList.item[requests[pokemon]].grid(column=i % 4, row=int(i / 4), padx=20)
            i += 1

    def search(self):

        self.pokeList.destroy()

        self.pokeList = ctk.CTkFrame(master=self)
        self.pokeList.grid(column=0, columnspan=3, row=1, sticky="nswe")
        self.pokeList.columnconfigure((0, 1, 2, 3), weight=1)
        self.pokeList.rowconfigure((0, 1, 2), weight=1)

        string = self.searchbar.get()

        if string != "":

            self.pokeList.item = {}

            pokemons = get_all_pokemon(lenght=905)

            for poke in pokemons.keys():
                i = len(self.pokeList.item)
                if i >= 12:
                    break
                elif re.match(r"" + string, pokemons[poke], re.IGNORECASE):
                    self.pokeList.item[pokemons[poke]] = PokeCard(poke, pokemons[poke], master=self.pokeList,
                                                                  edit=self.edit, pokemon_number=self.pokemon_number)
                    self.pokeList.item[pokemons[poke]].grid(column=i % 4, row=int(i / 4))

        else:
            self.drawPage()


class PokeCard(ctk.CTkFrame):
    def __init__(self, id, name, edit, pokemon_number, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.edit = edit
        self.pokemon_number = pokemon_number
        self.id = id
        self.name = name
        self.configure(corner_radius=15, border_width=1, border_color="white")

        if self.edit:
            self.add = ctk.CTkButton(master=self, text="Ajouter", fg_color=self.fg_color, text_color='green', border_color='green', border_width=1,
                                     hover_color=self.bg_color, command=partial(self.add_team, self.name), width=50)
            self.add.pack()
            self.add.place(relx=0.65, rely=0.1)

        self.image = ctk.CTkButton(master=self, image=getPixelSprite(id), text="", fg_color=self.fg_color,
                                   hover=False, command=self.clicked, corner_radius=15)
        self.image.grid(column=0, padx=(5, 0), pady=(5, 0))

        self.title = ctk.CTkLabel(master=self, text=self.name)
        self.title.grid(column=1, padx=(0, 6), pady=(0, 6))

        self.columnconfigure((0, 2), weight=1)
        self.columnconfigure(1, weight=5)

        self.bind("<Button-1>", self.clicked)

    def clicked(self):
        self.master.master.master.frame_right.destroy()
        self.master.master.master.frame_right = PokemonPage(self.id, master=self.master.master.master)
        self.master.master.master.frame_right.setup()

    def add_team(self, pokemon_name):
        local_storage.LocalStorage().set_data(item=self.pokemon_number, value=pokemon_name)
        print(self.pokemon_number)
        print(pokemon_name)
        print(local_storage.LocalStorage().get_data(item=self.pokemon_number))

        self.master.master.master.frame_right.destroy()
        from pages.team_add_page import TeamAddPage
        self.master.master.master.frame_right = TeamAddPage()
        self.master.master.master.frame_right.setup()
