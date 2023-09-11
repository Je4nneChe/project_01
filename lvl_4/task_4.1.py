# Задача 4.1.
# Домашнее задание на SQL
# В базе данных teacher создайте таблицу Students
# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)
# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.
# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

# Создаю таблицу School:
connection= sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """CREATE TABLE School(
School_Id INTEGER NOT NULL PRIMARY KEY,
School_Name TEXT NOT NULL, 
Place_Count INTEGER NOT NULL);"""
cursor.execute(query)
connection.commit()
connection.close()
#  наполняю таблицу School:
connection= sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO School (School_Id, School_Name, Place_Count)
VALUES
('1', 'Протон', 200),
('2', 'Преспектива', 300),
('3', 'Спектр', 400),
('4', 'Содружество', 500);"""
cursor.execute(query)
connection.commit()
connection.close()

# Создаю таблицу Students:
connection= sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY);"""
cursor.execute(query)
connection.commit()
connection.close()
# Наполнение таблицу Students:
connection= sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO Students(Student_Id, Student_Name, School_Id)
VALUES
(201, 'Иван', 1),
(202, 'Петр', 2),
(203, 'Анастасия', 3),
(204, 'Игорь', 4);"""
cursor.execute(query)
connection.commit()
connection.close()

# 1 вариант решения:

def get_connection():                                                 # функция подключения к БД
    connection = sqlite3.connect('teatchers.db')                      # переменная для подключения к БД
    return connection
def close_connection(connection):                                     # функция отключения от БД
    if connection:
        connection.close()                                            # закрываем соединение с БД

def get_school_name(school_id):                                       # функция для вывода имени школы
    try:
        connection = get_connection()                                 # исполняю функцию get_connection()
        cursor = connection.cursor()                                  # определяю курсор
        select_query = """SELECT * FROM School WHERE School_Id = ?""" # задаю переменную с SQL запросом
                                                                      # (значение из таб School - School_Id (Primary key))
        cursor.execute(select_query, (school_id,))                    # курсором выполняю запрос для извлечения рез-та
        record = cursor.fetchone()                                    # присваиваю переменной record вывод результата 
        close_connection(connection)                                  # закрываю соединение с БД
        return record[1]                                              # возвращаем результат, где 1 - это индекс в списке значений по студенту
    except(Exception, sqlite3.Error) as error:                        # если будет исключение, код не сработает
        print("Ошибка в получении данных по школе ", error)           # и выведет ошибку
    
def get_student(student_id):                                          # получим данные по студенту по его ID
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """SELECT * FROM Students WHERE Student_Id = ?""" # задаю переменную с SQL запросом
                                                                      # (значение из таб Students - Student_Id)
        cursor.execute(select_query, (student_id,))                   # курсором выполняю запрос для извлечения рез-та 
        records = cursor.fetchall()                                   # присваиваю переменной record вывод всех результатов 
        for row in records:                                           # для строки в выводе
            print ("ID студента", row[0])                             # печатаю ...., где  0 индекс в списке значений по студенту
            print ("Имя студента", row[1])                            # печатаю ...., где  1 индекс в списке значений по студенту
            print ("ID школы", row[2])                                # печатаю ...., где  2 индекс в списке значений по студенту
            print ("Название школы", get_school_name(row[2]))         # печатаю ...., где  2 индекс в списке значений по школе
        close_connection(connection)                                  # закрываю соединение с БД
    except (Exception, sqlite3.Error) as error:                       # если будет исключение, код не сработает
        print ("Ошибка в получении данных ", error)                   # и выведет ошибку
get_student(202)                                                      # получаем студента по ID (ID в скобках) 

# если не показать создание таблицы School, то название школы будет неизвестно
# и при поиске ошибок выведится - Ошибка в получении данных  name 'get_school_name' is not defined.
# если введенного ID студента нет в таб.студентов, то код не сработает
# если ошибка внутри def get_student(student_id):, то выведится - Ошибка ........

# 2 вариант решения через оператор JOIN (короче):

def get_connection():                                                  # функция подключения к БД
    connection = sqlite3.connect('teatchers.db')                       # переменная для подключения к БД
    return connection
def close_connection(connection):                                      # функция отключения от БД
    if connection:
        connection.close()                                             # закрываем соединение с БД

def get_student(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """SELECT * FROM Students JOIN School ON School.School_Id = Students.School_Id WHERE Students.Student_Id=?"""
        cursor.execute (query,(student_id,))
        records = cursor.fetchall()
        for row in records:
            print("ID студента:", row[0])
            print("Имя студента:", row[1])
            print("ID школы:", row[2])   
            print("Название школы:", row[4],'\n')
    except (Exception, sqlite3.Error) as error:
        print ('Ошибка в получении данных', error)
get_student(203)

# запрос """SELECT * FROM Students JOIN School ON School.School_Id = Students.School_Id WHERE Students.Student_Id=?"""
# означает: выбираем всю таб. Students, присоединяем таб. School по условию - поле School_Id в таб.School 
# должно соответсвовать полю School_Id в таб.Students, где ID студента и запрашиваем.