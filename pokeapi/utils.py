from pokeapi.api import PokeAPI
from pokeapi.db.db import PokemonDatabase

def fetch_pokemon_data(pokemon_id):
    api = PokeAPI()
    return api.fetch_pokemon_data(pokemon_id)

def store_pokemon_data(database, pokemon_data):
    database.insert_pokemon(pokemon_data)

def get_pokemon_data(database):
    return database.get_pokemon()