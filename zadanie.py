import sqlite3
import random

db = sqlite3.connect('z2.db')

cursor = db.cursor()


cursor.execute(f"""INSERT INTO table1(c1, c2) VALUES ({random.randint(0,9)}, {random.randint(0,9)});""",)

db.commit()

cursor.execute("""SELECT * FROM table1""")
a = cursor.fetchall()

cursor.execute("""SELECT COUNT(*) FROM table1""")
b = cursor.fetchall()
b = b[0][0]
count = 0
sum = 0
for j in range(b):
    id = 0
    try:
        for i in range(3):
            if type(a[id][i]) == int:
                sum += a[id][i]
        id += 1
        count += 1
    except:
        pass

sa = sum / count

if sa > count:
    cursor.execute("""delete from table1 where id=4;""")
cursor.close()
db.close()import sqlite3
import random

db = sqlite3.connect('z2.db')

cursor = db.cursor()


cursor.execute(f"""INSERT INTO table1(c1, c2) VALUES ({random.randint(0,9)}, {random.randint(0,9)});""",)

db.commit()

cursor.execute("""SELECT * FROM table1""")
a = cursor.fetchall()

cursor.execute("""SELECT COUNT(*) FROM table1""")
b = cursor.fetchall()
b = b[0][0]
count = 0
sum = 0
for j in range(b):
    id = 0
    try:
        for i in range(3):
            if type(a[id][i]) == int:
                sum += a[id][i]
        id += 1
        count += 1
    except:
        pass

sa = sum / count

if sa > count:
    cursor.execute("""delete from table1 where id=4;""")
cursor.close()
db.close()