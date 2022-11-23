import tkinter

import pokebase as pb
import utils.requests_pokemon as api
import io
from PIL import Image,ImageTk


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
        self.type = poke['types'][0]['type']['name']

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