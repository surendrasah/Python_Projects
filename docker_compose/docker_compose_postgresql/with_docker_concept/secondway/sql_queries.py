select_cocktails = """ SELECT name FROM cocktails WHERE name = %s """

update_cocktails = """ UPDATE cocktails SET ingredients = %s, instructions = %s, glass_type = %s WHERE name = %s """

insert_cocktails = """ INSERT INTO cocktails (name, ingredients, instructions, glass_type) VALUES (%s, %s, %s, %s) """

fetchall_cocktails = """ SELECT * FROM cocktails LIMIT 2; """
