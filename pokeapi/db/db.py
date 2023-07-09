import psycopg2

class PokemonDatabase:
    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    def connect(self):
        connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.username,
            password=self.password
        )
        return connection

    def create_table(self):
        connection = self.connect()
        cursor = connection.cursor()
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS pokemon (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                height NUMERIC,
                weight NUMERIC
            )
        '''
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        connection.close()

    def insert_pokemon(self, pokemon):
        connection = self.connect()
        cursor = connection.cursor()
        insert_query = '''
            INSERT INTO pokemon (name, height, weight)
            VALUES (%s, %s, %s)
        '''
        values = (
            pokemon['name'],
            pokemon['height'],
            pokemon['weight']
        )
        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
        connection.close()

    def get_pokemon(self):
        connection = self.connect()
        cursor = connection.cursor()
        select_query = '''
            SELECT * FROM pokemon
        '''
        cursor.execute(select_query)
        pokemon = cursor.fetchall()
        cursor.close()
        connection.close()
        return pokemon
