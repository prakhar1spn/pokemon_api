import requests

class PokeAPI:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2'

    def fetch_pokemon_data(self, pokemon_id):
        url = f'{self.base_url}/pokemon/{pokemon_id}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to fetch Pokémon data from the PokéAPI')
