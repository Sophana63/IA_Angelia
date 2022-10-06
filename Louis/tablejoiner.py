import sqlite3
import os
import time
from sqlite3 import Error

db = sqlite3.connect("Sources_data.db")
c = db.cursor()

def timetranslate(t) :
    s = t
    m = s // 60
    s = s % 60
    h = m // 60
    m = m % 60
    d = h // 24
    h = h % 24
    text = ["","","",""]
    if (d > 1) :
        text[0] = str(d) + " days, "
    elif (d == 1) :
        text[0] = str(d) + " day, "
    else :
        text[0] = ""
    if (h > 9) :
        text[1] = str(h) + "h"
    elif (d > 0 or h > 0) :
        text[1] = "0" + str(h) + "h"
    else :
        text[1] = ""
    if (m > 9) :
        text[2] = str(m) + ":"
    else :
        text[2] = "0" + str(m) + ":"
    if (s > 9) :
        text[3] = str(s)
    else :
        text[3] = "0" + str(s)
    return ("".join(text))
    
def loadbar(cent) :
    bar = []
    for foo in range (25) :
        bar.append(' ')
    for full in range (cent // 4) :
        bar[full] = '█'
    if (cent % 4 == 3) :
        bar[(cent // 4)] = '▓'
    elif (cent % 4 == 2) :
        bar[(cent // 4)] = '▒'
    elif (cent % 4 == 1) :
        bar[(cent // 4)] = '░'
    return ("".join(bar))


popa = input("Popularity requested for 'artistes': (0-100)")
popc = input("Popularity requested for 'chansons': (0-100)")

rqa = "SELECT name, id, popularity FROM 'artistes' WHERE popularity >= " + str(popa)
c.execute(rqa)
artists = c.fetchall()

chansons = []
eta_start = time.time()
for i in range (len(artists)) :
    cur_id = artists[i][1]
    ##print(cur_id)
    rqb = ("SELECT name, id, popularity FROM 'chansons' WHERE id_artists LIKE '%" + cur_id + "%' AND popularity >= " + str(popc))
    c.execute(rqb)
    albums = c.fetchall()
    ##print(albums)
    for j in range (len(albums)) :
        chansons.append([albums[j], artists[i]])

    eta_cur = time.time() - eta_start
    eta_past = int(eta_cur)
    eta_left = eta_cur * len(artists) / (i+1) - eta_cur
    eta_left = int(eta_left)
    percentint = (i * 100) // len(artists)
    loadingbar = loadbar(percentint)
    percent = str(percentint)
    if (percentint < 10) :
        percent = " " + percent
    if (i % 4 == 0) :
        spinny = "|"
    elif (i % 4 == 1) :
        spinny = "/"
    elif (i % 4 == 2) :
        spinny = "-"
    elif (i % 4 == 3) :
        spinny = "\\"

    os.system("cls")
    print("Albuming...   " + spinny)
    print("[" + loadingbar + "] " + percent + "%   (" + str(i+1) + "/" + str(len(artists)) + ")")
    print("Time elapsed  : " + timetranslate(eta_past))
    print("Time remaining: " + timetranslate(eta_left))

os.system("cls")
try :
    rqc =   """CREATE TABLE hits (
                id_chanson TEXT REFERENCES chansons(id) NOT NULL,
                id_artist TEXT REFERENCES artistes(id) NOT NULL,
                name TEXT NOT NULL,
                song_popularity INTEGER NOT NULL,
                artist TEXT NOT NULL,
                artist_popularity INTEGER NOT NULL,
                PRIMARY KEY (id_chanson, id_artist)
            );"""
    c.execute(rqc)
    db.commit()

except sqlite3.Error as error :
    if (str(error) == "table hits already exists") :
        try :
            rqd = "DELETE FROM hits"
            c.execute(rqd)
            db.commit()
        except sqlite3.Error as error :
            print("ERROR:\ncouldn't reset table")
            print(error)
    else :
        print("ERROR:\ncouldn't create table")
        print(error)

os.system("cls")
eta_start = time.time()
try :
    for k in range (len(chansons)) :
        try :
            rqe = 'INSERT INTO hits VALUES ("' + str(chansons[k][0][1]) + '", "' + str(chansons[k][1][1]) + '", "' + str(chansons[k][0][0]) + '", ' + str(chansons[k][0][2]) + ', "' + str(chansons[k][1][0]) + '", ' + str(chansons[k][1][2]) + ');'
            c.execute(rqe)
            db.commit()

            eta_cur = time.time() - eta_start
            eta_past = int(eta_cur)
            eta_left = eta_cur * len(chansons) / (k+1) - eta_cur
            eta_left = int(eta_left)
            percentint = (k * 100) // len(chansons)
            loadingbar = loadbar(percentint)
            percent = str(percentint)
            if (percentint < 10) :
                percent = " " + percent
            if ((k // 10) % 4 == 0) :
                spinny = "|"
            elif ((k // 10) % 4 == 1) :
                spinny = "/"
            elif ((k // 10) % 4 == 2) :
                spinny = "-"
            elif ((k // 10) % 4 == 3) :
                spinny = "\\"

            os.system("cls")
            print("Setting table...   " + spinny)
            print("[" + loadingbar + "] " + percent + "%   (" + str(k+1) + "/" + str(len(chansons)) + ")")
            print("Time elapsed  : " + timetranslate(eta_past))
            print("Time remaining: " + timetranslate(eta_left))
        except sqlite3.Error as error :
            print("ERROR:\ncouldn't set table on item " + str(k))
            print(error)
            break
except :
    print("")
else :
    os.system("cls")
    print("Done! 👍\n[" + loadbar(100) + "]100%")
    print(str(len(chansons)) + " hits with\n    'artistes' popularity: " + str(popa) + "\nand 'chansons' popularity: " + str(popc))

#os.system("cls")
#print("\n\n---- FULL LIST: ----\n")
#for p in range (len(chansons)) :
    #print(chansons[p])
