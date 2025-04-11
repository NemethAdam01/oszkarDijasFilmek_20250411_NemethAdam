import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "oscar"
)
mycursor = mydb.cursor()

#2. feladat
mycursor.execute("SELECT ev, cim FROM film WHERE nyert = 1 ORDER BY ev ASC")
for x in mycursor:
    print(x)
#3. feladat
mycursor.execute("SELECT ev FROM film GROUP BY ev HAVING COUNT(ev) >= 10")
for x in mycursor:
    print(x)
#4.feladat
mycursor.execute("SELECT * FROM film WHERE bemutato BETWEEN 1939-01-01 AND 1945-12-31")
for x in mycursor:
    print(x)