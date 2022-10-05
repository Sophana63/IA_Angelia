import sqlite3
import statistics

#relier la BDD à notre code
bdd = sqlite3.connect('Desktop\db\Sources_data.db')
cur = bdd.cursor()

#Faire une moyenne, en se référant à notre BDD
Time_moy_2020 = "select AVG(time_signature) from chansons where release_date like 2020 order by popularity desc limit 50"
cur.execute(Time_moy_2020)

#resultat Time signature
res_Time_moy_2020 = cur.fetchall()
print(res_Time_moy_2020)