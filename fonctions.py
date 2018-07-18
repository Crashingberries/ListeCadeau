import sqlite3
from tkinter import *

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

def CreationTableProduitListe():
    commande_sql = """CREATE TABLE `ProduitsListe` (
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
    curseur.execute(commande_sql,(client))
    connexionDB.commit()

def AjoutProduitListe(ClientID,Cup):
    produitAjout=[]
    commande_sql= ("""SELECT FC_Title_Short FROM EnsembleProduit WHERE EAN = (?);""")
    curseur.execute(commande_sql,(Cup,))
    produitAjout.append(curseur.fetchall())
    if(produitAjout[0]==[]):
        return "Le code de produit entrée est invalide!"
    else:
        commande_sql= ("""SELECT Price FROM EnsembleProduit WHERE EAN = (?);""")
        curseur.execute(commande_sql,(Cup,))
        produitAjout.append(curseur.fetchall())
        commande_sql ="""INSERT INTO ProduitsListe(ClientID,CUP,NomProduit,Prix,Achete)
        VALUES (?,?,?,?,?);"""
        curseur.execute(commande_sql,(str(ClientID),Cup,str(produitAjout[0]),str(produitAjout[1]),0))
        connexionDB.commit()

def RechercheClient(NomClient):
    ensembleresultats=[]
    commande_sql=("""SELECT Id,Nom,Adresse,DateDeFete FROM Clients WHERE Nom= ?""")
    curseur.execute(commande_sql,(NomClient,))
    resultat=curseur.fetchall()
    for ligne in resultat:
       ensembleresultats.append(ligne)
    return (resultat)

def RechercheListe(IdClient):
    ensembleresultats=[]
    commande_sql=("""SELECT CUP,NomProduit,Prix FROM ProduitsListe WHERE ClientID= ?""")
    curseur.execute(commande_sql,(IdClient,))
    resultat=curseur.fetchall()
    for ligne in resultat:
        #test= [tuple(s if type(s)!=int or s!="(" or s!=")" or s!="'" or s!="[" or s!="]"  else "" for s in tup) for tup in ligne]
        ensembleresultats.append(ligne)
    return (resultat)

def ModifierClient(InfoClient,NouvellesInformations):
    commande_sql=("""UPDATE Clients SET Nom=?,Adresse=?,DateDeFete=? WHERE ID= ?""")
    curseur.execute(commande_sql,(NouvellesInformations[0],NouvellesInformations[1],NouvellesInformations[2],InfoClient[0],))
    connexionDB.commit()

def EffacerProduitListe(IdClient,CupProduitAEffacer):
    commande_sql=("""DELETE FROM ProduitsListe WHERE ClientID= ? AND CUP=? AND Achete=0""")
    curseur.execute(commande_sql,(IdClient,CupProduitAEffacer,))
    connexionDB.commit()



CreationTableClient()
CreationTableProduitListe()
