import sqlite3
import pandas as pd

#Connect to SQLite database
conn = sqlite3.connect('osm.db')
#create the cursor
cursor = conn.cursor()
#read the csv file, location is as per container folder: /app/osm_python/
df_osm = pd.read_csv('osm.csv', index_col=0) #index_col=0 while reading to remove Unnamed: 0

#load data to osm table
df_osm.to_sql('osm', conn, if_exists='replace',index=False) #while writing index=False for no index

cursor.execute(''' SELECT * FROM osm limit 100''')

# Fetch the result
result = cursor.fetchmany(5)

# Print the result
print(result)

#number of distinct cities in the data set?
cursor.execute("SELECT COUNT(DISTINCT City) FROM osm")
# Fetch the result
city_result = cursor.fetchone()[0]

# Print the result
print("No. of distinct city : ",city_result)

#number of distict street in the data set?
cursor.execute("SELECT COUNT(DISTINCT Street) FROM osm")
# Fetch the result
street_result = cursor.fetchone()[0]

# Print the result
print("No. of distinct street : ",street_result)

# Close the cursor and connection
conn.commit()
cursor.close()
conn.close()


