from tkinter import PhotoImage
import customtkinter as ctk

from models import pokemon_model
from utils import ui_kits
from utils.images import download_file


class PokemonPage(ctk.CTkFrame):

    def __init__(self, pokemon_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.pokemon_id = pokemon_id
        self.current_pokemon = pokemon_model.Pokemon(pokemon_id)

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11), weight=1)
        self.rowconfigure(12, weight=0)
        self.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.columnconfigure(5, weight=0)

    def setup(self):
        # Pokemon image
        img = download_file(self.current_pokemon.spriteUrlHighQuality).subsample(3, 3)

        self.master.pokemon_image = ui_kits.img(self, img)
        self.master.pokemon_image.grid(row=0, column=2)

        #  id
        self.master.label_id = ctk.CTkLabel(master=self, text="Id : " + str(self.current_pokemon.id_formatted),
                                            corner_radius=5
                                            )
        self.master.label_id.grid(row=1, column=2)

        #  name
        self.master.label_name = ctk.CTkLabel(master=self, text="Name : " + str(self.current_pokemon.name))
        self.master.label_name.grid(row=2, column=2)

        # type
        self.master.label_type = ctk.CTkLabel(master=self, text="Type : " + str(self.current_pokemon.type))
        self.master.label_type.grid(row=3, column=2)

        # STATS AREA

        # HP
        self.master.label_hp = ctk.CTkLabel(master=self, text="Heatlh :" + str(self.current_pokemon.hp))
        self.master.label_hp.grid(row=4, column=2)

        # Attack
        self.master.label_attack = ctk.CTkLabel(master=self, text="Attack : " + str(self.current_pokemon.attack))
        self.master.label_attack.grid(row=5, column=2)

        # Defense
        self.master.label_defense = ctk.CTkLabel(master=self, text="Defense : " + str(self.current_pokemon.defense))
        self.master.label_defense.grid(row=6, column=2)

        # Sp Attack
        self.master.label_sp_attack = ctk.CTkLabel(master=self,
                                                   text="Special Attack : " + str(self.current_pokemon.sp_attack))
        self.master.label_sp_attack.grid(row=7, column=2)

        # Sp Defense
        self.master.label_sp_defense = ctk.CTkLabel(master=self,
                                                    text="Special Defense : " + str(self.current_pokemon.sp_defense))
        self.master.label_sp_defense.grid(row=8, column=2)

        # Speed
        self.master.label_speed = ctk.CTkLabel(master=self, text="Speed : " + str(self.current_pokemon.speed))
        self.master.label_speed.grid(row=9, column=2)

        # Total Stats
        self.master.label_total_stats = ctk.CTkLabel(master=self,
                                                     text="Puissance : " + str(self.current_pokemon.total_stats))
        self.master.label_total_stats.grid(row=10, column=2)

        # Arrow change Pokémons

        arrow_left = PhotoImage(file="./img/arrow_left.png").subsample(12, 12)
        self.master.button_arrow_left = ctk.CTkButton(master=self, text="",
                                                      image=arrow_left,
                                                      fg_color=self.fg_color,
                                                      command=self.pokemon_previous,
                                                      hover=False)
        self.master.button_arrow_left.grid(row=11, column=0)

        arrow_right = PhotoImage(file="./img/arrow_right.png").subsample(12, 12)
        self.master.button_arrow_right = ctk.CTkButton(master=self, text="",
                                                       image=arrow_right,
                                                       fg_color=self.fg_color,
                                                       command=self.pokemon_next,
                                                       hover=False)
        self.master.button_arrow_right.grid(row=11, column=4)

    def pokemon_previous(self):

        if self.pokemon_id <= 1:
            return

        next_pokemon = self.pokemon_id - 1
        self.destroy()
        self.master.frame_right = PokemonPage(pokemon_id=next_pokemon)
        self.master.frame_right.setup()

    def pokemon_next(self):

        if self.pokemon_id >= 905:
            return

        next_pokemon = self.pokemon_id + 1
        self.destroy()
        self.master.frame_right = PokemonPage(pokemon_id=next_pokemon)
        self.master.frame_right.setup()
