import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
import sqlite3
from sqlite3 import Error

import plotly_express as px

from app import app,server

app = dash.Dash(__name__)

#End_Import

con = sqlite3.connect('db\Sources_data.db')
cur = con.cursor()

#create dataFrame for plotly_express

cur.execute ("SELECT genre, COUNT(song) as nb_song, song, date FROM songs_genres GROUP BY date, genre ORDER BY date ASC")
df = pd.DataFrame(cur.fetchall(), columns=['genre', 'nb-song', 'song', 'date'])
print(df)

cur.execute("SELECT genre, COUNT(song) as nb_song FROM songs_genres GROUP BY genre ORDER BY nb_song DESC LIMIT 37")
df_song = pd.DataFrame(cur.fetchall(), columns=['genre', 'nb_song'])
print(df_song)

years = []
#year = 1988
for i in range(1979,2022):
    years.append(i)
    

if __name__ == '__main__':


    app = dash.Dash(__name__) 


    fig = px.scatter(df, x= "date", y="nb-song",

                        color = "genre",                        
                        size="nb-song",
                        category_orders={"date": years},
                        hover_name="nb-song") 

    fig2 = px.scatter(df_song, x= "genre", y="nb_song",

                        color = "genre",                        
                        size="nb_song",
                        hover_name="nb_song")

    app.layout = html.Div(children=[


                            html.H1(children=f'Liste des genres par année',

                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)


                            dcc.Graph(

                                id='graph1',

                                figure=fig

                            ), # (6)


                            html.Div(children=f'''

                                Nuage de points représentant le nombre de titre de même genre de 1979 
                                à 2021. Toutes les chansons sont récupérées sur les 50 artistes les
                                plus populaires. Ce graphique nous montre une tendance de genre par 
                                période. Avant les années 2000, le genre Hoerspiel est le plus représenté.
                                De 2001 à 2017, la Pop est au dessus des autres. Et en ce moment, le Trap Latino 
                                et le Reggaeton cartonnent.

                            '''), # (7)

                            html.H1(children=f'Liste des genres par titre',

                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)


                            dcc.Graph(

                                id='graph2',

                                figure=fig2

                            ), # (6)


                            html.Div(children=f'''

                                Test....graph en cours

                            '''), # (7)


    ]

    )


    #
    # RUN APP
    #
    app.run_server(debug=True) # (8)
