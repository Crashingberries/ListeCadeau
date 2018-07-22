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

def AjoutClient(Enfant):
    commande_sql ="""INSERT INTO Clients(Nom,Adresse,DateDeFete)
    VALUES (?,?,?);"""
    client= (Enfant.Nom,Enfant.Adresse,Enfant.DateDeFete)
    curseur.execute(commande_sql,(client))
    commande_sql="""SELECT ID FROM Clients ORDER BY ID DESC LIMIT 1;"""
    curseur.execute(commande_sql)
    temp=(curseur.fetchall())
    temp=str(temp[0])
    temp=temp[1:temp.find(",")]
    connexionDB.commit()
    return temp

def AjoutProduitListe(ClientID,Produit):
    produitAjout=[]
    commande_sql= ("""SELECT FC_Title_Short FROM EnsembleProduit WHERE EAN = (?);""")
    curseur.execute(commande_sql,(Produit.Cup,))
    produitAjout.append(curseur.fetchall())
    if(produitAjout[0]==[]):
        return "Le code de produit entrée est invalide!"
    else:
        commande_sql= ("""SELECT Price FROM EnsembleProduit WHERE EAN = (?);""")
        curseur.execute(commande_sql,(Produit.Cup,))
        produitAjout.append(curseur.fetchall())
        commande_sql ="""INSERT INTO ProduitsListe(ClientID,CUP,NomProduit,Prix,Achete)
        VALUES (?,?,?,?,?);"""
        Produit.ModifierNom(str(produitAjout[0]))
        Produit.ModifierPrix(str(produitAjout[1]))
        print(str(Produit))
        curseur.execute(commande_sql,(ClientID,Produit.Cup,Produit.Nom,Produit.Prix,0))
        connexionDB.commit()

def RechercheClient(NomClient):
    ensembleresultats=[]
    commande_sql=("""SELECT Nom,Adresse,DateDeFete,Id FROM Clients WHERE Nom LIKE ? """)
    NomClient+="%"
    curseur.execute(commande_sql,(NomClient,))
    resultat=curseur.fetchall()
    return resultat

def RechercheListe(IdClient,Valeur=0):
    ensembleresultats=[]
    commande_sql=("""SELECT NomProduit,Prix,CUP FROM ProduitsListe WHERE ClientID= ? AND Achete=?""")
    curseur.execute(commande_sql,(IdClient,Valeur,))
    resultat=curseur.fetchall()
    return (resultat)

def ModifierClient(InfoClient,NouvellesInformations):
    commande_sql=("""UPDATE Clients SET Nom=?,Adresse=?,DateDeFete=? WHERE ID= ?""")
    curseur.execute(commande_sql,(NouvellesInformations[0],NouvellesInformations[1],NouvellesInformations[2],InfoClient[0],))
    connexionDB.commit()

def EffacerProduitListe(IdClient,CupProduitAEffacer):
    commande_sql=("""DELETE FROM ProduitsListe WHERE ClientID= ? AND CUP=? AND Achete=0""")
    curseur.execute(commande_sql,(IdClient,CupProduitAEffacer,))
    connexionDB.commit()

def InfoClient(Client):
    commande_sql=("""SELECT Nom FROM Clients WHERE ID= ?""")
    curseur.execute(commande_sql,(Client.Id,))
    Client.Nom=curseur.fetchall()
    commande_sql=("""SELECT Adresse FROM Clients WHERE ID= ?""")
    curseur.execute(commande_sql,(Client.Id,))
    Client.Adresse=curseur.fetchall()
    commande_sql=("""SELECT DateDeFete FROM Clients WHERE ID= ?""")
    curseur.execute(commande_sql,(Client.Id,))
    Client.DateDeFete=curseur.fetchall()
    return Client

def ChangerListeCadeau(IdClient,CupProduitAChanger,Valeur):
    commande_sql=("""UPDATE ProduitsListe SET Achete=? WHERE ClientID= ? AND CUP=? """)
    curseur.execute(commande_sql,(Valeur,IdClient,CupProduitAChanger,))
    connexionDB.commit()



CreationTableClient()
CreationTableProduitListe()
