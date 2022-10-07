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



