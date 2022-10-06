from turtle import width
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics



plt.style.use('_mpl-gallery')
bdd = sqlite3.connect('db\Sources_data.db')
cur = bdd.cursor()

# tableau fait par Sophana 
# date = 2015
# for i in range(0,3):
#        date = 2015 + i
#        text_date = str(date)
#        req = "SELECT loudness, name, popularity FROM chansons WHERE release_date LIKE '%" + text_date + "%' GROUP BY name, loudness ORDER BY popularity DESC  LIMIT 10 "
#        cur.execute(req)
#        print(cur.fetchall())

#_____________________________________________________________________________loud 2015
loud_moy_2015 = "select (loudness) from chansons Where release_date like '%2015%' order by popularity desc limit 50"
cur.execute(loud_moy_2015)
#resutat loud
res_loud_2015 = cur.fetchall()
# print(res_loud_2015)

# étape 1, passer de tuples à une liste de float 
a = list(res_loud_2015)
a = []
for i in range(0,len(res_loud_2015)):
    a.append(list(res_loud_2015[i]))

list_res_loud_2015 = []
for i in range(0,len(res_loud_2015)):
    list_res_loud_2015.append(a[i][0])
list_res_loud_2015

#trouver la moy et la dev standard 
moyenne_b = statistics.mean(list_res_loud_2015)
moy_loud_moy_2015 = statistics.mean(list_res_loud_2015)
print(moy_loud_moy_2015)
stdev_loud_moy_2015 = statistics.stdev(list_res_loud_2015)
print(stdev_loud_moy_2015)

#_____________________________________________________________________________________loud 2016
loud_2016 = "select (loudness) from chansons Where release_date like '%2016%' order by popularity desc limit 50"
cur.execute(loud_2016)
#variable
res_loud_2016 = cur.fetchall()
# print(res_loud_2016)

#tuple to float list 
a2016 = list(res_loud_2016)
a2016 = []
for i in range(0,len(res_loud_2016)):
    a2016.append(list(res_loud_2016[i]))
a2016

list_res_loud_2016 = []
for i in range(0,len(res_loud_2016)):
    list_res_loud_2016.append(a2016[i][0])
list_res_loud_2016

#trouver la moy et la dev standard 
moy_loud_2016 = statistics.mean(list_res_loud_2016)
print(moy_loud_2016)
stdev_loud_moy_2016 = statistics.stdev(list_res_loud_2016)
print(stdev_loud_moy_2016)

#_____________________________________________________________________________loud 2017
loud_2017 = "select (loudness) from chansons Where release_date like '%2017%' order by popularity desc limit 50"
cur.execute(loud_2017)
#resutat loud
res_loud_2017 = cur.fetchall()
# print(res_loud_moy_2017)

#tuple to float list 
a2017 = list(res_loud_2017)
a2017 = []
for i in range(0,len(res_loud_2017)):
    a2017.append(list(res_loud_2017[i]))
a2017

list_res_loud_2017 = []
for i in range(0,len(res_loud_2017)):
    list_res_loud_2017.append(a2017[i][0])
list_res_loud_2017

#trouver la moy et la dev standard 
moy_loud_2017 = statistics.mean(list_res_loud_2017)
print(moy_loud_2017)
stdev_loud_moy_2017 = statistics.stdev(list_res_loud_2017)
print(stdev_loud_moy_2017)

#________________________________________________________________loud 2018
loud_2018 = "select (loudness) from chansons Where release_date like '%2018%' order by popularity desc limit 50"
cur.execute(loud_2018)
#resutat loud
res_loud_2018 = cur.fetchall()
print(res_loud_2018)

#tuple to float list 
a2018 = list(res_loud_2018)
a2018 = []
for i in range(0,len(res_loud_2018)):
    a2018.append(list(res_loud_2018[i]))
a2018

list_res_loud_2018 = []
for i in range(0,len(res_loud_2018)):
    list_res_loud_2018.append(a2018[i][0])
list_res_loud_2018

#trouver la moy et la dev standard 
moy_loud_2018 = statistics.mean(list_res_loud_2018)
print(moy_loud_2018)
stdev_loud_moy_2018 = statistics.stdev(list_res_loud_2018)
print(stdev_loud_moy_2018)

#________________________________________________________________loud 2019
loud_2019 = "select (loudness) from chansons Where release_date like '%2019%' order by popularity desc limit 50"
cur.execute(loud_2019)
#resutat loud
res_loud_2019 = cur.fetchall()
print(res_loud_2019)

#tuple to float list 
a2019 = list(res_loud_2019)
a2019 = []
for i in range(0,len(res_loud_2019)):
    a2019.append(list(res_loud_2019[i]))
a2019

list_res_loud_2019 = []
for i in range(0,len(res_loud_2019)):
    list_res_loud_2019.append(a2019[i][0])
list_res_loud_2019

#trouver la moy et la dev standard 
moy_loud_2019 = statistics.mean(list_res_loud_2019)
print(moy_loud_2019)
stdev_loud_moy_2019 = statistics.stdev(list_res_loud_2019)
print(stdev_loud_moy_2019)

#________________________________________________________________loud 2020
loud_2020 = "select (loudness) from chansons Where release_date like '%2020%' order by popularity desc limit 50"
cur.execute(loud_2020)
#resutat loud
res_loud_2020 = cur.fetchall()
print(res_loud_2020)

#tuple to float list 
a2020 = list(res_loud_2020)
a2020 = []
for i in range(0,len(res_loud_2020)):
    a2020.append(list(res_loud_2020[i]))
a2020

list_res_loud_2020 = []
for i in range(0,len(res_loud_2020)):
    list_res_loud_2020.append(a2020[i][0])
list_res_loud_2020

#trouver la moy et la dev standard 
moy_loud_2020 = statistics.mean(list_res_loud_2020)
print(moy_loud_2020)
stdev_loud_moy_2020 = statistics.stdev(list_res_loud_2020)
print(stdev_loud_moy_2020)

#________________________________________________________________loud 2021
loud_2021 = "select (loudness) from chansons Where release_date like '%2021%' order by popularity desc limit 50"
cur.execute(loud_2021)
#resutat loud
res_loud_2021 = cur.fetchall()
print(res_loud_2021)

#tuple to float list 
a2021 = list(res_loud_2021)
a2021 = []
for i in range(0,len(res_loud_2021)):
    a2021.append(list(res_loud_2021[i]))
a2021

list_res_loud_2021 = []
for i in range(0,len(res_loud_2021)):
    list_res_loud_2021.append(a2021[i][0])
list_res_loud_2021

#trouver la moy et la dev standard 
moy_loud_2021 = statistics.mean(list_res_loud_2021)
print(moy_loud_2021)
stdev_loud_moy_2021 = statistics.stdev(list_res_loud_2021)
print(stdev_loud_moy_2021)

liste = [list_res_loud_2015, list_res_loud_2016, list_res_loud_2017, list_res_loud_2018, list_res_loud_2019, list_res_loud_2020, list_res_loud_2021]
# combine these different collections into a list    
data_to_plot = liste

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

#Create an axes instance
ax = fig.add_subplot(121)

ax.set_xticklabels(['2015', '2016', '2017', '2018','2019', '2020', '2021'])

# Create the boxplot
bp = ax.boxplot(data_to_plot)

plt.title('Intensité (en db par années)')


# Save the figure
fig.savefig('diag_loud.png', bbox_inches='tight')
plt.show()
