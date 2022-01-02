import os,sys,sqlite3
if os.path.exists("firma1.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)
connection = sqlite3.connect("firma1.db")
cursor  = connection.cursor()
sql ="CREATE TABLE personen("\
    "name TEXT, "\
    "vorname TEXT, "\
    "personalnummer INTEGER PRIMARY KEY, "\
    "gehalt FLOAT, "\
    "geburtstag TEXT )"
cursor.execute(sql)
sql = "INSERT INTO personen VALUES('Taller', "\
    "'Mans',6000,2500,'10.01.1970')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO personen VALUES('Schmidt', "\
    "'Peter',86714,4500,'25.04.1958')"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO personen VALUES('Bayer', "\
    "'Julia',2287,3750,'30.12.1959')"
cursor.execute(sql)
connection.commit()


connection.close()

