import sqlite3
import numpy as np
from sqlite3 import Error

#from matplotlib import artist
con = sqlite3.connect('db\Sources_data.db')

cur = con.cursor()

request_genre = "select genres from par_genres_o GROUP BY genres"
request_2020 = "select id, name, genres, popularity FROM artistes ORDER BY popularity DESC LIMIT 50"

cur.execute(request_genre)
all_genres = cur.fetchall()
cur.execute(request_2020)
s = cur.fetchall()

try :
    rqc =   """CREATE TABLE top50 (
                id_chanson TEXT REFERENCES chansons(id) NOT NULL,
                id_artist TEXT REFERENCES artistes(id) NOT NULL,
                name TEXT NOT NULL,
                song_popularity INTEGER NOT NULL,
                song_date TEXT NOT NULL,
                artist TEXT NOT NULL,
                artist_popularity INTEGER NOT NULL,
                artist_genres TEXT,
                PRIMARY KEY (id_chanson, id_artist)
            );"""
    cur.execute(rqc)
    con.commit()
except sqlite3.Error as error :
    if (str(error) == "table top50 already exists") :
        try :
            rqd = "DELETE FROM top50"
            cur.execute(rqd)
            con.commit()
        except sqlite3.Error as error :
            print("ERROR:\ncouldn't reset table")
            print(error)
    else :
        print("ERROR:\ncouldn't create table")
        print(error)

listes = []
for i in range(len(s)):
    artiste = s[i][0]
    req_artist = "select id, name, popularity, release_date FROM chansons WHERE id_artists like '%" + artiste + "%' "
    cur.execute(req_artist)
    artist_music = cur.fetchall()
    for j in range (len(artist_music)):
        listes.append([s[i], artist_music[j]])

print(listes)
for k in range (len(listes)):
    print(str(listes[k][1][1]).replace('"', "'"))
    req_insert = 'INSERT INTO top50 VALUES ("' + str(listes[k][1][0]) + '", "' + str(listes[k][0][0]) + '","' + str(listes[k][1][1]).replace('"', "'") + '","' + str(listes[k][1][2]) + '","' + str(listes[k][1][3]) + '", "' + str(listes[k][0][1]) + '","' + str(listes[k][0][3]) + '", "' + str(listes[k][0][2]) + '")'
    cur.execute(req_insert)
    con.commit()
    
"""
k = 0
for j in range (len(s)):
    genre = s[j][0]
    text = str(genre).strip('[]')
    req_genre_artist = "select COUNT(genres), genres FROM par_genres_o WHERE genres IN (" + text + ")"    
    cur.execute(req_genre_artist)
    res_genre_artist = cur.fetchall()
    print(res_genre_artist)
    k = k + 1
    
        
print(k)
"""

    #print(artist_music, id_artist)

        

    




#cur.execute(request_2020)
#print(cur.fetchall())

