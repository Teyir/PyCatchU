import tkinter

import utils.requests_pokemon as api
import io
from PIL import Image,ImageTk


def format_id(pokemon_id):
    if pokemon_id > 999:
        return "#" + str(pokemon_id)
    elif pokemon_id > 99:
        return "#0" + str(pokemon_id)
    elif pokemon_id > 9:
        return "#00" + str(pokemon_id)
    else:
        return "#000" + str(pokemon_id)


class Pokemon:
    def __init__(self, id_or_name):
        if type(id_or_name) == int:
            id_or_name = str(id_or_name)
        poke = api.get_pokemon(id_or_name)
        species = api.get_pokemon_species(id_or_name)
        self.id = poke['id']
        self.name = poke['name']
        self.spriteUrlPixel = poke['sprites']['front_default']
        self.spriteUrlHighQuality = poke['sprites']['other']['official-artwork']['front_default']
        self.color = species['color']['name']
        # Stats
        self.type = poke['types'][0]['type']['name']
        self.hp = poke['stats'][0]['base_stat']
        self.weight = poke['weight']
        self.attack = poke['stats'][1]['base_stat']
        self.defense = poke['stats'][2]['base_stat']
        self.sp_attack = poke['stats'][3]['base_stat']
        self.sp_defense = poke['stats'][4]['base_stat']
        self.speed = poke['stats'][5]['base_stat']
        self.total_stats = self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed

        self.id_formatted = format_id(pokemon_id=self.id)

    def getPixelSprite(self):
        raw_data = api.get_image(self.spriteUrlPixel)
        im = Image.open(raw_data)
        return ImageTk.PhotoImage(im)

    def getHighQualitySprite(self):
        raw_data = api.get_image(self.spriteUrlHighQuality)
        im = Image.open(raw_data)
        return ImageTk.PhotoImage(im)


    def __str__(self):
        return "#" + str(self.id) + " : " + self.name
