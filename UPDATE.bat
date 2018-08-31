@echo off
IF EXIST item_listings_local_matches.csv (
sqlite3 ListeCadeau.db < bin/commandes.txt && ECHO Importation complete avec succes! &&^
DEL *.csv)^
ELSE (ECHO Echec de la Mise a Jour. Ficher CSV non present.)
PAUSE