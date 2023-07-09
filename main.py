import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from pokeapi.api import PokeAPI
from pokeapi.db.db import PokemonDatabase
from pokeapi.utils import fetch_pokemon_data, store_pokemon_data, get_pokemon_data

app = FastAPI()

class Pokemon(BaseModel):
    id: int
    name: str
    types: list[str]

def transform_pokemon_data(pokemon_data):
    """
    Transforms the Pokémon data.
    """
    df = pd.DataFrame(pokemon_data, columns=['id', 'name', 'type1', 'type2'])
    df['types'] = df[['type1', 'type2']].values.tolist()
    df.fillna('None', inplace=True)
    transformed_data = df.to_dict('records')
    
    return transformed_data

@app.post("/pokemon")
def fetch_and_store_pokemon_data(pokemon_id: int):
    """
    Fetches and stores Pokémon data for a given ID.
    """
    try:
        pokemon_data = fetch_pokemon_data(pokemon_id)
        store_pokemon_data(db, pokemon_data)
        return {"message": f"Stored Pokémon data for ID: {pokemon_id}"}
    except Exception as e:
        return {"message": f"Failed to fetch/store Pokémon data for ID: {pokemon_id}", "error": str(e)}

@app.get("/pokemon")
def get_stored_pokemon_data():
    """
    Retrieves stored Pokémon data.
    """
    stored_pokemon = get_pokemon_data(db)
    transformed_data = transform_pokemon_data(stored_pokemon)
    return {"pokemon": transformed_data}

if __name__ == "__main__":
    
    DB_HOST="localhost"
    DB_PORT=5432
    DB_NAME="pokemon_data"
    DB_USERNAME="postgres"
    DB_PASSWORD="$$$$$$$$$"
    
    db = PokemonDatabase(host=DB_HOST, port=DB_PORT, database=DB_NAME, username=DB_USERNAME, password=DB_PASSWORD)
    db.create_table()  
    uvicorn.run(app, host="0.0.0.0", port=8000)
