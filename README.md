# pokemon_api
The provided code sets up a web API using FastAPI to fetch, transform, and store Pokémon data. It utilizes the PokeAPI to fetch Pokémon data based on a given ID and stores it in a PostgreSQL database. 

POST /pokemon: This endpoint fetches and stores Pokémon data for a specified ID. It receives a request with a Pokémon ID, fetches the corresponding data from the PokeAPI, and stores it in the PostgreSQL database using the store_pokemon_data function. If successful, it returns a message indicating that the Pokémon data has been stored.

GET /pokemon: This endpoint retrieves the stored Pokémon data from the PostgreSQL database. It fetches the data using the get_pokemon_data function, transforms it using the transform_pokemon_data function, and returns the transformed data in the response.
