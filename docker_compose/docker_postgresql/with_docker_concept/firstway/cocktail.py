import psycopg2
import requests
import json

try:
    # Set up database connection
    conn = psycopg2.connect(
        host="db",
        database="cocktaildb",
        user="postgres",
        password="postgres"
    )
except Exception as e:
    print(e)
    exit(0)

if conn is not None:
    print("connection established to postgresql")
    cur = conn.cursor()
    print('connection established ', cur)
    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cocktails (
            name TEXT PRIMARY KEY,
            ingredients TEXT,
            instructions TEXT,
            glass_type TEXT
        );
    """)
    conn.commit()

    # Fetch cocktails from API
    response = requests.get("https://us-central1-nexible-code.cloudfunctions.net/cocktails")
    data = response.json()

    cocktail_list = []
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

        conn.commit()

    print("cocktails detail")
    cur.execute("""SELECT * FROM cocktails LIMIT 2;""")
    for record in cur.fetchall():
        print('name = ', record[0], ', ingredients = ', record[1], ', instructions = ', record[2],
              ', glass_type = ', record[3])

    cur.close()
    conn.close()

else:
    print("connection not establish to postgresql")
