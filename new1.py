import os
import time

data = ['hello', 1023, 'hoho', 56, 6321, 'PyCharm', 7, 'nice', "дом", 3, 5]
def write_to_file(data):
    # Сортируем список слов по их длине
    words = sorted([item for item in data if isinstance(item, str)], key=len)
    # Сортируем список чисел в порядке возрастания
    numbers = sorted([item for item in data if isinstance(item, int)])
    # Записываем слова в файл
    with open('work.txt', 'w', encoding='utf-8') as file:
        for word in words: file.write(word + '\n')
        # Записываем числа в файл
        for number in numbers: file.write(str(number) + '\n')
longest_string = max([item for item in data if isinstance(item, str)], key=len)
write_to_file(data) # Записываем данные в файл
os.mkdir(longest_string)  # Создаем папку с названием самой длинной строки
time.sleep(2) # ждём 10 секунд
os.rmdir(longest_string) # Удаляем папку

