import mysql.connector
# permet de se connecter au serveur de base de donnée.

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)
print(mydb)

# plus simple pour la suite .
mycursor = mydb.cursor()

# permet de creer la base de donnée si elle est pas créer .
mycursor.execute("CREATE DATABASE IF NOT EXISTS slender")

mydb.commit()

# Ferme la connection au serveur.
mydb.close()
