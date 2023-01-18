from flask import Flask
import json
import sqlite3
app = Flask(__name__)

@app.route('/row/<string:id>', methods=['GET'])
def get_row(id):
    conn = sqlite3.connect('./data/osm.db')  #../osm_python/osm.db incase of different directories
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM osm WHERE id=?", (id,))
    row = cursor.fetchone()
    return json.dumps(row, ensure_ascii=False) #return original string

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
