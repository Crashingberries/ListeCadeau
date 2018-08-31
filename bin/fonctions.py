"""
Version 1.0
Alex Thibeault

Ce fichier regroupe l'ensembles des fonctions qui communique avec la base de données.
"""

import sqlite3
from tkinter import *

connexionDB = sqlite3.connect('ListeCadeau.db')
curseur = connexionDB.cursor()

def CreationTableClient():
#Sert à Créer la table Client en cas de première ouverture du programme. Si la
#table existe déjà, la fonction évite d'écraser la table présente.

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
#Même concept que CreationTableClient mais pour la Table ProduitListe

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

def CreationTableDBProduit():
#Même concept que CreationTableClient mais pour la Table DBProduit

    commande_sql= """CREATE TABLE `DBProduit` (
	`TEMP`	INTEGER NOT NULL);"""
    try:
        curseur.execute(commande_sql)
    except sqlite3.OperationalError:
        pass


def AjoutClient(Enfant):
#Permet d'ajouter un Client dans la base de données.

#Paramètres:
#Enfant: Un objet de type 'Enfant' regroupant les informations necessaire pour
#        ajouter un Client à la base de données.

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
#Permet d'ajouter un produit dans la table ProduitListe. Cette Table regroupe
#l'entièreté des produits reliés à un compte client.

#Paramètres:
#ClientID: Le ID unique d'un client. C'est ce qui permet de faire la différence
#          entre un compte et un autre.
#Produit: Un objet de type 'Produit' qui regroupe toutes les informations du
#         produit à ajouter.


    produitAjout=[]
    commande_sql= ("""SELECT Item FROM DBProduit WHERE UPC = (?);""")
    curseur.execute(commande_sql,(Produit.Cup,))
    produitAjout.append(curseur.fetchall())
    if(produitAjout[0]==[]):
        return "Le code de produit entrée est invalide!"
    else:
        commande_sql= ("""SELECT Price FROM DBProduit WHERE UPC = (?);""")
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

def ModifierClient(IdClient,Enfant):
    commande_sql=("""UPDATE Clients SET Nom=?,Adresse=?,DateDeFete=? WHERE ID= ?""")
    Enfant.ModifierNom(Enfant.Nom)
    Enfant.ModifierAdresse(Enfant.Adresse)
    Enfant.ModifierDateDeFete(Enfant.DateDeFete)
    curseur.execute(commande_sql,(Enfant.Nom,Enfant.Adresse,Enfant.DateDeFete,IdClient,))
    connexionDB.commit()

def EffacerProduitListe(IdClient,CupProduitAEffacer):
    commande_sql=("""DELETE FROM ProduitsListe WHERE Achete=0 AND EntreeNo=(SELECT EntreeNo FROM ProduitsListe WHERE ClientID= ? AND CUP=? LIMIT 1)""")
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
    commande_sql=("""UPDATE ProduitsListe SET  Achete=? WHERE EntreeNo= (SELECT EntreeNo FROM ProduitsListe WHERE ClientID= ? AND CUP=?  AND Achete!=? LIMIT 1)""")
    curseur.execute(commande_sql,(Valeur,IdClient,CupProduitAChanger,Valeur,))
    connexionDB.commit()

def SupprimerClientDB(IdClient):
    commande_sql=("""DELETE FROM Clients  WHERE ID=? """)
    curseur.execute(commande_sql,(IdClient,))
    commande_sql=("""DELETE FROM ProduitsListe  WHERE ClientID=? """)
    curseur.execute(commande_sql,(IdClient,))
    connexionDB.commit()



CreationTableClient()
CreationTableProduitListe()
CreationTableDBProduit()
