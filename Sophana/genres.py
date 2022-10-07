import sqlite3
import numpy as np
from sqlite3 import Error

#from matplotlib import artist
con = sqlite3.connect('db\Sources_data.db')
cur = con.cursor()

delete_tb = "DROP TABLE songs_genres"
cur.execute(delete_tb)
con.commit()
try :
    rqc =   """CREATE TABLE songs_genres (
                id_chanson TEXT NOT NULL,
                song TEXT NOT NULL,
                genre TEXT NOT NULL,
                date TEXT NOT NULL
            );"""
    cur.execute(rqc)
    con.commit()
except sqlite3.Error as error :
    if (str(error) == "table songs_genres already exists") :
        try :
            rqd = "DELETE FROM songs_genres"
            cur.execute(rqd)
            con.commit()
        except sqlite3.Error as error :
            print("ERROR:\ncouldn't reset table")
            print(error)
    else :
        print("ERROR:\ncouldn't create table")
        print(error)

request = "SELECT id_chanson, name, artist_genres, song_date FROM top50"
cur.execute(request)

songs = cur.fetchall()

for i in range (len(songs)):
    genres = songs[i][2]  
    list_genres = genres.strip('[]').split(",")
    
    for j in range (len(list_genres)):    
        print(list_genres[j])
        req_insert = 'INSERT INTO songs_genres VALUES ("' + str(songs[i][0]) + '", "' + str(songs[i][1]) + '", ' + list_genres[j] + ', "' + str(songs[i][3]) + '")' 
        cur.execute(req_insert)
        con.commit()

