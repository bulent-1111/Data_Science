import os,sys,sqlite3
if os.path.exists("firma.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)
connection = sqlite3.connect("firma.db")
cursor  = connection.cursor()
sql ="CREATE TABLE personen("\
    "name TEXT, "\
    "vorname TEXT, "\
    "personalnummer INTEGER PRIMARY KEY, "\
    "gehalt FLOAT, "\
    "geburtstag TEXT )"
cursor.execute(sql)
sql = "INSERT INTO personen VALUES('Maler', "\
    "'Hnas',6714,3500,'15.03.1962')"
cursor.execute(sql)
connection.commit()
connection.close()

