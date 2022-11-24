import requests
import re

def get_pokemons_amount():
    url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=1'
    res = requests.get(url).json()
    return res['count']


def get_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=' + get_pokemons_amount()
    return requests.get(url).json()


def get_pokemon(id_or_name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + id_or_name
    req = requests.get(url)

    if req.text == "Not Found":
        req = requests.get('https://pokeapi.co/api/v2/pokemon/905')

    return req.json()


def get_pokemon_species(id_or_name):
    url = 'https://pokeapi.co/api/v2/pokemon-species/' + id_or_name
    req = requests.get(url)

    if req.text == "Not Found":
        req = requests.get('https://pokeapi.co/api/v2/pokemon-species/905')

    return req.json()


def get_image(url):
    return requests.get(url, stream=True).raw

def get_all_pokemon(page = 1, lenght = 0):

    len

    if page < 1 :
        url = "https://pokeapi.co/api/v2/pokemon/?limit=100000&offset=0"
    else:
        url = "https://pokeapi.co/api/v2/pokemon/?limit=50&offset=" + str((page-1)*50)
    response = {}
    for poke in requests.get(url).json()["results"]:
        response[int(re.search(r"(?<=pokemon/)[0-9]+",poke["url"]).group(0))] = poke["name"]

    return response
