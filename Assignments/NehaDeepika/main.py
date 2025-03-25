import sqlite3
connection=sqlite3.connect('database.db')
cursor=connection.cursor()

#Create
cursor.execute('create table balance(Acc_no int(10),Name varchar(120),Pin int(10),Net_balance float(10,2))')
print('Table created successfully')
cursor.execute("insert into balance (Acc_no,Name,Pin,Net_balance) values(100,'Deepthi',1234,0)")
cursor.execute("insert into balance values(101,'Eva',2345,100000)")
cursor.execute("insert into balance values(102,'Raghavendra',3456,110000)")
cursor.execute("insert into balance values(103,'Sthuthi',4567,85000)")
cursor.execute("insert into balance values(104,'Sujay',5678,50500)")
connection.commit()