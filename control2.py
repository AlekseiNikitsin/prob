import sqlite3
conn = sqlite3.connect('nado_practica.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table ( id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
city TEXT)
''')
cursor.executemany('''
INSERT INTO my_table(id,name,age,city) VALUES (?,?,?,?)''',[
    (1,'asd',11,'zxcv'),
    (2,'wrtwt',30,'uyt'),
    (3,'ufyytu',56,'trrerd')])
conn.commit()
conn.close()