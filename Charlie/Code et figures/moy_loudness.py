import sqlite3
import statistics
import matplotlib.pyplot as plt
import numpy as np


bdd = sqlite3.connect('db\Sources_data.db')
cur = bdd.cursor()
# MOY loud 2015
loud_moy_2015 = "select AVG(loudness) from chansons Where release_date like '%2015%' order by popularity desc limit 50"
cur.execute(loud_moy_2015)
#resutat loud
res_loud_moy_2015 = cur.fetchall()
print(res_loud_moy_2015)

# MOY loud 2016
loud_moy_2016 = "select AVG(loudness) from chansons Where release_date like '%2016%' order by popularity desc limit 50"
cur.execute(loud_moy_2016)
#resutat loud
res_loud_moy_2016 = cur.fetchall()
print(res_loud_moy_2016)

# MOY loud 2017
loud_moy_2017 = "select AVG(loudness) from chansons Where release_date like '%2017%' order by popularity desc limit 50"
cur.execute(loud_moy_2017)
#resutat loud
res_loud_moy_2017 = cur.fetchall()
print(res_loud_moy_2017)

# MOY loud 2018
loud_moy_2018 = "select AVG(loudness) from chansons Where release_date like '%2018%' order by popularity desc limit 50"
cur.execute(loud_moy_2018)
#resutat loud
res_loud_moy_2018 = cur.fetchall()
print(res_loud_moy_2018)

# MOY loud 2019
loud_moy_2019 = "select AVG(loudness) from chansons Where release_date like '%2019%' order by popularity desc limit 50"
cur.execute(loud_moy_2019)
#resutat loud
res_loud_moy_2019 = cur.fetchall()
print(res_loud_moy_2019)

# MOY loud 2020
loud_moy_2020 = "select AVG(loudness) from chansons Where release_date like '%2020%' order by popularity desc limit 50"
cur.execute(loud_moy_2020)
#resutat loud
res_loud_moy_2020 =  cur.fetchall()
print(res_loud_moy_2020)

# MOY loud 2021
loud_moy_2021 = "select AVG(loudness) from chansons Where release_date like '%2021%' order by popularity desc limit 50"
cur.execute(loud_moy_2021)
#resutat loud
res_loud_moy_2021 =  cur.fetchall()
print(res_loud_moy_2021)

# pour le diagramme en barres 
plt.style.use('_mpl-gallery')



plt.plot([2015, 2016, 2017, 2018, 2019, 2020, 2021], 
[-7.573671796808613, -7.2545737616168715, -7.215648296086573, -7.390116770299863, -7.434020240194789, -7.533984716940546, -7.898172265562792])



plt.title('Moyenne intensité par années (en db)')

plt.show()