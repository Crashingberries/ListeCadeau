
import sqlite3

connexionDB = sqlite3.connect('ListeCadeau.db')
curseur = connexionDB.cursor()

def CreationTableClient():
    commande_sql = """CREATE TABLE Clients (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom VARCHAR(40),
    Adresse VARCHAR(120),
    DateDeFete DATE);"""

    try:
        curseur.execute(commande_sql)
    except sqlite3.OperationalError:
        pass

def CreationTableProduit():
    commande_sql = """CREATE TABLE `Produits` (
	`EntreeNo`	INTEGER NOT NULL,
	`ClientID`	INTEGER NOT NULL,
	`CUP`	INTEGER,
	`NomProduit`	TEXT,
	`Prix`	FLOAT,
	`Achete`	BOOLEAN,
	PRIMARY KEY(`EntreeNo`),
	FOREIGN KEY(`ClientID`) REFERENCES `Clients`(`ID`));"""
    
    try:
        curseur.execute(commande_sql)
    except sqlite3.OperationalError:
      pass

def AjoutClient( nom,adresse,date):
    commande_sql ="""INSERT INTO Clients(Nom,Adresse,DateDeFete)
    VALUES (?,?,?);"""
    client= (nom,adresse,date)
    curseur.execute(commande_sql,client)
    connexionDB.commit()

#def AjoutProduit(Client):

CreationTableClient()
CreationTableProduit()
