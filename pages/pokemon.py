import tkinter
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

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.rowconfigure(7, weight=0)
        self.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.columnconfigure(5, weight=0)

    def setup(self):

        # Pokemon image
        img = download_file(self.current_pokemon.spriteUrlHighQuality).subsample(3, 3)

        self.frame_Image = ctk.CTkFrame(master=self, width=200, height=200, corner_radius=5, fg_color=self.fg_color)
        self.frame_Image.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        self.master.pokemon_image = ui_kits.img(self.frame_Image, img)
        self.master.pokemon_image.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #  id
        self.frame_Id = ctk.CTkFrame(master=self, width=100, height=40, corner_radius=5)
        self.frame_Id.grid(row=1, column=2, padx=5, pady=5)

        self.master.label_id = ctk.CTkLabel(master=self.frame_Id, text=self.current_pokemon.id_formatted)
        self.master.label_id.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #  name
        self.frame_Name = ctk.CTkFrame(master=self, width=200, height=40, corner_radius=5)
        self.frame_Name.grid(row=0, column=4, padx=5, pady=5, sticky="ne")

        self.master.label_name = ctk.CTkLabel(master=self.frame_Name, text="Name : " + str(self.current_pokemon.name))
        self.master.label_name.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # type
        self.frame_Type = ctk.CTkFrame(master=self, width=200, height=40, corner_radius=5)
        self.frame_Type.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        self.master.label_type = ctk.CTkLabel(master=self.frame_Type, text="Type : " + str(self.current_pokemon.type))
        self.master.label_type.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # STATS AREA

        # HP
        self.frame_Hp = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5)
        self.frame_Hp.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        self.master.label_hp = ctk.CTkLabel(master=self.frame_Hp, text="Heatlh : " + str(self.current_pokemon.hp))
        self.master.label_hp.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Attack
        self.frame_Att = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5)
        self.frame_Att.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        self.master.label_attack = ctk.CTkLabel(master=self.frame_Att, text="Attack : " + str(self.current_pokemon.attack))
        self.master.label_attack.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Defense
        self.frame_Def = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5)
        self.frame_Def.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

        self.master.label_defense = ctk.CTkLabel(master=self.frame_Def, text="Defense : " + str(self.current_pokemon.defense))
        self.master.label_defense.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Sp Attack
        self.frame_sp_att = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5)
        self.frame_sp_att.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        self.master.label_sp_attack = ctk.CTkLabel(master=self.frame_sp_att,
                                                   text="Special Attack : " + str(self.current_pokemon.sp_attack))
        self.master.label_sp_attack.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Sp Defense
        self.frame_sp_def = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5)
        self.frame_sp_def.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

        self.master.label_sp_defense = ctk.CTkLabel(master=self.frame_sp_def,
                                                    text="Special Defense : " + str(self.current_pokemon.sp_defense))
        self.master.label_sp_defense.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Speed
        self.frame_sp_spd = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5)
        self.frame_sp_spd.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

        self.master.label_speed = ctk.CTkLabel(master=self.frame_sp_spd, text="Speed : " + str(self.current_pokemon.speed))
        self.master.label_speed.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Total Stats
        self.frame_pow = ctk.CTkFrame(master=self, width=200, height=20, corner_radius=5)
        self.frame_pow.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

        self.master.label_total_stats = ctk.CTkLabel(master=self.frame_pow,
                                                     text="Total Power : " + str(self.current_pokemon.total_stats))
        self.master.label_total_stats.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

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
