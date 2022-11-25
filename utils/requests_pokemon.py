import requests
import re
from PIL import Image,ImageTk

def get_pokemons_amount():
    url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=1'
    res = requests.get(url).json()
    return res['count']


def get_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=905'
    return requests.get(url).json()


def get_pokemon(id_or_name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + id_or_name
    req = requests.get(url)

    if req.text == "Not Found":
        req = requests.get('https://pokeapi.co/api/v2/pokemon/905')

    return req.json()

def get_pokemon_sprite(name):
    link = get_pokemon(name)['sprites']['front_default']
    im = Image.open(link)
    return ImageTk.PhotoImage(im)


def get_pokemon_species(id_or_name):
    url = 'https://pokeapi.co/api/v2/pokemon-species/' + id_or_name
    req = requests.get(url)

    if req.text == "Not Found":
        req = requests.get('https://pokeapi.co/api/v2/pokemon-species/905')

    return req.json()


def get_image(url):
    return requests.get(url, stream=True).raw


def get_all_pokemon(page=1, lenght=None):
    if lenght is None:
        lenght = 50

    lenght = str(lenght)
    if page < 1:
        url = "https://pokeapi.co/api/v2/pokemon/?limit=100000&offset=0"
    else:
        page = str((page - 1) * int(lenght))
        url = "https://pokeapi.co/api/v2/pokemon/?limit=" + lenght + "&offset=" + page
    response = {}
    print(url)
    for poke in requests.get(url).json()["results"]:
        response[int(re.search(r"(?<=pokemon/)[0-9]+", poke["url"]).group(0))] = poke["name"]

    return response


def getPixelSprite(id):
    raw_data = get_image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+str(id)+".png")
    im = Image.open(raw_data)
    return ImageTk.PhotoImage(im)

