# Installation


## Base de données

Il faudra récupérer la base de données SQLITE (Sources_data.db) sur le brief Angelia de Simplon Online et le copier dans le dossier /db.

[Lien simplonline](https://simplonline.co/login)


## Création des tables 

- Executer le fichier connect_bdd.py pour créer la table songs_artists.
- Executer le fichier genres.py pour la table songs_genres
- Executer le fichier update_db.py pour modifier la colonne "date" de type 'text' en 'integer'


## Installation des librairies

```bash
conda install -c anaconda sqlite
conda install -c conda-forge dash
conda install -c conda-forge dash-core-components
conda install -c conda-forge dash-html-components
conda install -c anaconda pandas
conda install -c conda-forge numpy
conda install -c plotly plotly_express

```

## Visualisation du graphique

*Nuage de points représentant le nombre de titre de même genre de 1979 à 2021. Toutes les chansons sont récupérées sur les 50 artistes les plus populaires. Ce graphique nous montre une tendance de genre par période. Avant les années 2000, le genre Hoerspiel est le plus représenté. De 2001 à 2017, la Pop est au dessus des autres. Et en ce moment, le Trap Latino et le Reggaeton cartonnent. *
- Executer le fichier stat_genre_by_date.py pour afficher un nuage de points.



