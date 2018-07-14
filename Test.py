import sqlite3
connexionDB = sqlite3.connect('ListeCadeau.db')
curseur = connexionDB.cursor()

commande_sql = """CREATE TABLE emp ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);"""

curseur.execute(commande_sql)
