import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE band='Cats'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [("Catsss", "Cat Cityss")]

cursor.executemany("INSERT INTO events VALUES(?, ?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
