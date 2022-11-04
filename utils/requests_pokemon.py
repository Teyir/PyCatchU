import requests


def get_pokemons_amount():
    url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=1'
    res = requests.get(url).json()
    return res['count']


def get_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=' + get_pokemons_amount()
    return requests.get(url).json()


def get_pokemon(id_or_name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + id_or_name
    return requests.get(url).json()

def get_pokemon_species(id_or_name):
    url = 'https://pokeapi.co/api/v2/pokemon-species/' + id_or_name
    return requests.get(url).json()

def get_image(url):
    return requests.get(url,stream=True).raw