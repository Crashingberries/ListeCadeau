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
    commande_sql= ("""SELECT FC_Title_Short,Price FROM EnsembleProduit WHERE EAN = (?);""")
    curseur.execute(commande_sql,(Cup,))
    details=curseur.fetchall()
    for info in details:
        produitAjout=info
    commande_sql ="""INSERT INTO ProduitsListe(ClientID,CUP,NomProduit,Prix,Achete)
    VALUES (?,?,?,?,?);"""
    ajoutListe=(ClientID,Cup,produitAjout[0],produitAjout[1],0)
    curseur.execute(commande_sql,ajoutListe)
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
       ensembleresultats.append(ligne)
    return (resultat)


CreationTableClient()
CreationTableProduitListe()
