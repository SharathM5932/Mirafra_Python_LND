import sqlite3
db_name = "example.db"
connection=sqlite3.connect(db_name)
print(f"Database '{db_name}' created successfully.")
cursor=connection.cursor()
cursor.execute(""" create table if not exists student(name text,id integer primary key,fee real)""")
print("Table 'student' created successfully.")
cursor.execute("INSERT INTO student (name, id, fee) VALUES (?, ?, ?)", ("Rajesh", 1, 10.45))
cursor.execute("INSERT INTO student (name, id, fee) VALUES (?, ?, ?)", ("Ibrahim", 2, 11.234))
cursor.execute("INSERT INTO student (name, id, fee) VALUES (?, ?, ?)", ("Sahastra", 3, 12.23))
cursor.execute("INSERT INTO student (name, id, fee) VALUES (?, ?, ?)", ("Harsh", 4, 13.2))
print("Values inserted into table")

connection.commit()


connection.close()
print("Database connection closed.")