import sqlite3
conn = sqlite3.connect('asd.db')
cursor = conn.cursor()
cursor.execute('''create table if not exists tab_1(id integer primary key autoincrement, col_1 text,col_2 text)''')
cursor.execute('''insert into tab_1(col_1,col_2)values ('привет я почти разобрался','а может и нет')''')
conn.commit()
cursor.execute('''select*from tab_1''')
k = cursor.fetchall()
print(k)