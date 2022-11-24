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

    def setup(self):
        # Pokemon image
        img = download_file(self.current_pokemon.spriteUrlHighQuality).subsample(3, 3)

        self.master.pokemon_image = ui_kits.img(self, img)
        self.master.pokemon_image.place(relx=0.25, rely=0.25)

        # Pokemon name
        self.master.label_name = ctk.CTkLabel(master=self, text=self.current_pokemon.name)
        self.master.label_name.place(relx=0.2, rely=0.3)

        # Pokemon id
        self.master.label_id = ctk.CTkLabel(master=self, text=self.current_pokemon.id_formatted)
        self.master.label_id.place(relx=0.25, rely=0.3)

        # Pokémon type
        self.master.label_type = ctk.CTkLabel(master=self, text=self.current_pokemon.type)
        self.master.label_type.place(relx=0.25, rely=0.3)

        # STATS AREA

        # HP
        self.master.label_hp = ctk.CTkLabel(master=self, text=self.current_pokemon.hp)
        self.master.label_hp.place(relx=0.25, rely=0.3)

        # Attack
        self.master.label_attack = ctk.CTkLabel(master=self, text=self.current_pokemon.attack)
        self.master.label_attack.place(relx=0.25, rely=0.3)

        # Defense
        self.master.label_defense = ctk.CTkLabel(master=self, text=self.current_pokemon.defense)
        self.master.label_defense.place(relx=0.25, rely=0.3)

        # Sp Attack
        self.master.label_sp_attack = ctk.CTkLabel(master=self, text=self.current_pokemon.sp_attack)
        self.master.label_sp_attack.place(relx=0.25, rely=0.3)

        # Sp Defense
        self.master.label_sp_defense = ctk.CTkLabel(master=self, text=self.current_pokemon.sp_defense)
        self.master.label_sp_defense.place(relx=0.25, rely=0.3)

        # Speed
        self.master.label_speed = ctk.CTkLabel(master=self, text=self.current_pokemon.speed)
        self.master.label_speed.place(relx=0.25, rely=0.3)

        # Total Stats
        self.master.label_total_stats = ctk.CTkLabel(master=self, text=self.current_pokemon.total_stats)
        self.master.label_total_stats.place(relx=0.25, rely=0.3)

        # Arrow change Pokémons

        if self.pokemon_id > 1:
            arrow_left = PhotoImage(file="./img/arrow_left.png").subsample(12, 12)
            self.master.button_arrow_left = ctk.CTkButton(master=self, text="",
                                                          image=arrow_left,
                                                          fg_color=self.fg_color,
                                                          command=self.pokemon_previous,
                                                          hover=False)
            self.master.button_arrow_left.place(relx=0.08, rely=0.75)

        if self.pokemon_id < 905:
            arrow_right = PhotoImage(file="./img/arrow_right.png").subsample(12, 12)
            self.master.button_arrow_right = ctk.CTkButton(master=self, text="",
                                                           image=arrow_right,
                                                           fg_color=self.fg_color,
                                                           command=self.pokemon_next,
                                                           hover=False)
            self.master.button_arrow_right.place(relx=0.3, rely=0.75)

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
