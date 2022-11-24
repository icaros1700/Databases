import sqlite3

conn = sqlite3.connect('proyecto.db')
cursor = conn.cursor()

#cursor.execute("INSERT INTO inal(id, nombre, apellido) VALUES (2, 'Camilo', 'Ruiz')")

conn.commit()
rows = cursor.execute("SELECT * FROM inal")

for row in rows:
    print(row)


cursor.close()
conn.close()