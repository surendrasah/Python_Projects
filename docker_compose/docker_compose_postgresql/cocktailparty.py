#!/usr/bin/python
import requests
import json
import psycopg2
from config import config


class CockTailParty():
    def __init__(self):
        self.cocktail_list_url = "https://us-central1-nexible-code.cloudfunctions.net/cocktails"
        self.conn = self.db_connect()

    def cocktail_data_extraction(self):
        response = requests.get(self.cocktail_list_url)
        # load cocktail list to data
        data = json.loads(response.text)
        return data

    def cocktail_data_transform(self):
        cocktail_list = []
        data = self.cocktail_data_extraction()

        for cocktail in data:
            name = cocktail["name"]
            ingredients = cocktail["ingredients"]
            instructions = ""
            glass_type = ""

            # Extracting instructions and glass type from the given API
            inst_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
            inst_resp = requests.get(inst_url)
            inst_data = json.loads(inst_resp.text)
            # print("get requests:\n",inst_data)

            if inst_data["drinks"] != None:
                instructions = inst_data["drinks"][0]["strInstructions"]
                glass_type = inst_data["drinks"][0]["strGlass"]

            cocktail_dict = {"name": name, "ingredients": ingredients, "instructions": instructions,
                             "glass_type": glass_type}
            cocktail_list.append(cocktail_dict)
        # print(cocktail_list)
        return cocktail_list

    def db_connect(self):

        # Connect to the PostgreSQL database server
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            print('Connected to the PostgreSQL database')

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return conn

    def cocktail_etl(self):
        # call the data transformation
        cocktail_list = self.cocktail_data_transform()

        # create a cursor
        try:
            cur = self.conn.cursor()

            # Creating table to store the cocktail recipes
            cur.execute(
                "CREATE TABLE IF NOT EXISTS cocktails (name TEXT PRIMARY KEY, ingredients TEXT[], instructions TEXT, glass_type TEXT)")

            print("data is being inserted")
            # Inserting data into the table
            for cocktail in cocktail_list:
                name = cocktail["name"]
                ingredients = cocktail["ingredients"]
                instructions = cocktail["instructions"]
                glass_type = cocktail["glass_type"]

                # Check if a row with the same name already exists in the table
                cur.execute('SELECT name FROM cocktails WHERE name = %s', (name,))
                existing_row = cur.fetchone()

                if existing_row:
                    # If a row exists, update it
                    print("data  exists, so updating it")
                    cur.execute(
                        'UPDATE cocktails SET ingredients = %s, instructions = %s, glass_type = %s WHERE name = %s',
                        (ingredients, instructions, glass_type, name))
                else:
                    # If a row does not exist, insert a new row
                    cur.execute(
                        "INSERT INTO cocktails (name, ingredients, instructions, glass_type) VALUES (%s, %s, %s, %s)",
                        (name, ingredients, instructions, glass_type))

            print("cocktails detail")
            cur.execute("""SELECT * FROM cocktails LIMIT 2;""")
            for record in cur.fetchall():
                print('name = ', record[0], ', ingredients = ', record[1], ', instructions = ', record[2],
                      ', glass_type = ', record[3])

        except Exception as error:
            print(error)

        finally:
            if self.conn is not None:
                # Committing the changes to the database and closing the connection
                self.conn.commit()
                self.conn.close()
                print('Database connection closed.')


if __name__ == '__main__':
    party = CockTailParty()
    party.cocktail_etl()
