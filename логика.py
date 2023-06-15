import csv
import time
import json
import codecs
import psycopg2
from config import host, user, password, db_name

list_old_obj = []
try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True
#     # Создание таблицы
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE tasks(name varchar(100) NOT NULL, priority smallint NOT NULL, urgency date NOT null);"""
    #             # """INSERT INTO dailydo (description, priority, urgency) VALUES ('Oleg', 3, 2021-11-08)"""
    #     )
    #     print(cursor.fetchone())
    
#     # Создание новой строки данных
#     # with connection.cursor() as cursor:
#     #     cursor.execute(
#     #         """INSERT INTO tasks (name, priority, urgency) VALUES ('Новая задача', 6, '2020-10-05')"""
#     #     )
#     #     print(cursor.fetchone())
#     # Получение данных
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM tasks"
        )
        list_old_obj = cursor.fetchall()
except Exception as _ex:
    print('[INFO] Error while working with PostrgeSQL', _ex)
# finally:
#      if connection:
#           connection.close()
#           print("[INFO] PostgreSQL connection closed")


# Класс для задач, имеющий свойства описывающие задачу.
class Prioritet:
    count = 0
    list = []
    
    def __init__(self, name, priority, urgency):
        self.name = name
        self.priority = priority
        self.urgency = urgency
        Prioritet.count += 1
        self.list.append(self)
    def __str__(self):
        return f"{self.name, self.priority, self.urgency}"
    def __del__(self):
        # Удаление строк(запрос)
        # DELETE FROM tasks WHERE id = 5
        try:
            connection = psycopg2.connect(
                host = host,
                user = user,
                password = password,
                database = db_name
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""DELETE FROM tasks WHERE name = '{self.name}'"""
                )
            list_old_obj = cursor.fetchall()

        except Exception as _ex:
            print('[INFO] Error while working with PostrgeSQL', _ex)

# Получение данных из БД
for i in list_old_obj:
    a = Prioritet(i[0], i[1], i[2])

# try:
#     connection = psycopg2.connect(
#         host = host,
#         user = user,
#         password = password,
#         database = db_name
#     )
#     connection.autocommit = True

#     with connection.cursor() as cursor:
#         cursor.execute(
#             list_old_obj = "SELECT count(*) FROM tasks"
#         )
#         for i in list_old_obj:
#             cursor.execute(
#             a = Prioritet(f"SELECT * FROM tasks")
#             )
#         print(cursor.fetchall())
# except Exception as _ex:
#     print('[INFO] Error while working with PostrgeSQL', _ex)


# Функция для создания новой задачи
def new(name, priority, urgency):
    a = Prioritet(name, priority, urgency)
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
            )
        connection.autocommit = True
    # Создание новой строки данных
        with connection.cursor() as cursor:
            cursor.execute(
                f"""insert into tasks values ('{name}', {priority}, '{urgency}')"""
        )
        print(cursor.fetchone())
    except Exception as _ex:
        print('it was not possible to create and write an object to the database', _ex)

dict = {}
# new("Негры4", 3, '2024-04-04')

print(Prioritet.list)
# del Prioritet.list[0]


# Сортировка задач по важности
Prioritet.list = sorted(Prioritet.list, key=lambda x: x.priority)

# запись задач в словарь, где ключ - название, значения - все остальное
# for i in range(Prioritet.count):
#     dict[f'{Prioritet.list[i].name}']=f'{Prioritet.list[i].priority}', f'{Prioritet.list[i].urgency}'

    # dict.fromkeys(Prioritet.list[i].priority[Prioritet.list[i].priority])
    # print(Prioritet.list[i].priority)


# Запись в Json файл
# with open("tasks.json", "w", encoding='UTF-8') as file:
# 	json.dump(dict, file, indent = 4, ensure_ascii=False)

         
# Запись в CSV файл
# for i in Prioritet.list:
#     list_2 = [i.name, i.priority, i.urgency]
#     with open("information.csv", "a", newline='', encoding='UTF-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(list_2)



# t = []
# time1 = time.localtime(time.time())
# print(time.localtime(time.time()))
# # for i in range(0,8):
# #     t.append(time1[i])
# # print(t)
# time2 = time.mktime(time1)
# print(time2)
# print(prioritet.__dict__)


# Перетаскивание задачи
# Определение прогой приоритетов


# Сделать функцию автоматического добавления объекта из БД
# Сделать функцию удаления заметки из БД
