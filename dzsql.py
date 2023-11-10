import sqlite3
my_list = [1,'новая тема', 2,'домашнее задание',3,'штудируем инет', 4,'изучаем',5,'пытаемся разобраться'] # список содержащий числа и слова
conn = sqlite3.connect('Homework.db')#создание БД
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS text_table (id INTEGER PRIMARY KEY AUTOINCREMENT, text_data TEXT)''')#создание таблицы для текстовых данных
cursor.execute('''CREATE TABLE IF NOT EXISTS number_table (id INTEGER PRIMARY KEY AUTOINCREMENT, number_data INTEGER)''')#создание таблицы для числовых данных
for item in my_list:#обрабатываем элементы списка
    if isinstance(item,str):#если элемент - строка
        cursor.execute('INSERT INTO text_table (text_data) VALUES (?)',(item,))#записываем слово в твблицу text_table
        cursor.execute('INSERT INTO number_table (number_data) VALUES (?)', (len(item),))#записываем длину слова в таблицу number_table
    elif isinstance(item,int):#если элемент - число
        if item % 2 == 0: #если число четное
            cursor.execute('INSERT INTO number_table (number_data) VALUES (?)',(item,))
        else:#если число не четное
            cursor.execute('INSERT INTO text_table (text_data) VALUES (?)',(str(item),))
conn.commit()#сохраняем измененич в БД
conn.close()#закрываем соединение