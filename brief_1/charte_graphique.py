import sqlite3
import statistics

bdd = sqlite3.connect('db\Sources_data.db')
cur = bdd.cursor()

loud_moy = "select AVG(loudness) from chansons limit 50"
pop_moy = "select AVG(popularity) from chansons limit 50"
cur.execute(loud_moy)

#resutat loud
res_loud = cur.fetchall()
print(res_loud)

#resultat popolarity
cur.execute(pop_moy)
res_pop = cur.fetchall()
print(res_pop)

add = res_pop[0] + res_loud[0]
print(add)