import sqlite3
from sqlite3 import Error

con = sqlite3.connect('db\Sources_data.db')
cur = con.cursor()

for i in range(1978,2022):
    req = "UPDATE songs_genres SET date = " + str(i) + " WHERE date LIKE '%" + str(i) + "%'"
    cur.execute(req)
    con.commit()