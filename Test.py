import sqlite3
connexionDB = sqlite3.connect('ListeCadeau.db')
curseur = connexionDB.cursor()

commande_sql = """CREATE TABLE Clients (
ID INTEGER PRIMARY KEY,
Nom VARCHAR(40),
Adresse VARCHAR(120),
DateDeNaissance DATE,
DateDeFete DATE);"""

try  curseur.execute(commande_sql)

else
