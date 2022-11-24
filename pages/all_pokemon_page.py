import customtkinter as ctk

from models.pokemon_model import Pokemon
from pages.home_page import HomePage
from utils.requests_pokemon import get_all_pokemon



class AllPokemonPage(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

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

        self.pokeList.item = {}

        i = 0

        requests = get_all_pokemon(page=page, lenght=12)

        for pokemon in requests:
            o_pokemon = Pokemon(pokemon)
            self.pokeList.item[pokemon] = PokeCard(o_pokemon, master=self.pokeList)
            self.pokeList.item[pokemon].grid(column=i % 4, row=int(i / 4))
            i += 1


class PokeCard(ctk.CTkFrame):
    def __init__(self, o_Pokemon, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pokemon = o_Pokemon

        self.image = ctk.CTkButton(master=self, image=self.pokemon.getPixelSprite(), text="", fg_color=self.fg_color,
                                   hover=False)
        self.image.grid(column=0)

        self.title = ctk.CTkLabel(master=self, text=self.pokemon)
        self.title.grid(column=1)

        self.columnconfigure((0, 2), weight=1)
        self.columnconfigure(1, weight=5)

        self.bind("<Button-1>", self.clicked)
    def clicked(self):
        self.master.master.master.frame_right.destroy()
        self.master.master.master.frame_right = HomePage(master=self)
        self.master.master.master.frame_right.setup()
