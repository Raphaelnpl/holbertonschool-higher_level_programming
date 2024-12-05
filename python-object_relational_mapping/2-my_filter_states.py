#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création d'un curseur pour exécuter les requêtes
    cur = db.cursor()
    # Exécution de la requête SQL avec l'argument d'utilisateur pour le nom
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))

    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
