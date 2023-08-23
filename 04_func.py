# Функция - это блок кода, который можно вызывать с разными параметрами
# Функции - молотилки данных - внутрь помещаете значения, наа выходе получаете результат

employees_1 = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122988,
    'Frank' : 88123,
    'Eve' : 93121
    }
employees_2 = {
    'Nikita' : 1,
    'Masha' : 110000,
    'Matvey' : 90000,
    'Sasha' : 88123,
    'Tahya' : 193121
    }

# Этап создания функции
def get_topmgrs(empl):
    return [n for n, s in empl.items() if s >= 100000] # совмещение for и if 
    
# Этап вызова функции
get_topmgrs(employees_1)
get_topmgrs(employees_2)


# Воспользуемся результатом работы функции
print([employees_1[i]*1.5 for i in get_topmgrs(employees_1)])


# top_mgrs = [n for n, s in employees_1.items() if s >= 100000] # совмещение for и if 
# top_mgrs = [n for n, s in employees_2.items() if s >= 100000] # совмещение for и if 
# print(top_mgrs) 
 










# def add_root():
#     name = 'root'
#     uid = 0
#     return name, uid

# user_name, user_uiduid -add_root()    # ('root', 0)
#  #
#  #
#  # 1
# print ('Имя пользоватея', user_name, 'UID пользователя -')


# # 2


# # пример
# url = 'http://www.ranepa.ru/profile/login={}'.format('nikname')
# print(f'Имя пользователя - {user_name}\nUID пользователя - {user_uid}')


# # 3
# print(
#     f'Имя пользователя - {user_name}\nUID пользователя - {user_uid}'
#     )
# # пример 



# # Подробнее о функциях




# # при отладке интерпретатор записываеи имя функции и при вызове возвращается в нее
# # этап создания функции
# # параметры функции - данные на входе, которые нужно обработать внутри
# def greeting(name):
#     # Локальное пространство имен
#     print('Привет', name)

# # этап вызова функции
# # Глобальное пространство имен

# names = ['Мария', 'Матвей', 'Никита', 'Любовь']
# for i in names:     
#     greeting(i) 

# ############################################################


# # Подробнее о функциях
# # если навести на любую функцию, то увидим подробное описание
# # например print
#     # что такое "value"?
#     # как добавить описание? ОК
#     # именованные и позиционные параметры?
#     # чему равен параметр по умолчанию?
#     #

# # функция деления div(x - делимое, y - делитель)
# # 25 // 5 == 5


# def divide(dividend: int, divisor: int, ) -> int:
#     """
#     Функция divide принимает делимое и делитель в качестве параметров
#     и возвращат целое частное
#     """


#     quotient = 0

#     while diviend >= 0:
#         devidend -= divisor
#         quotient += 1

#     return quotient
#     print('Раздельтат деления', divide(100, 5))


# # именованные и позиционные параметры
# # параметры по умолчанию
# # явный вызов именованных параметров

# def trapezoid_s(a, b, *, h=1):
#     '''Функция для расчета площади трапеции. a - нижнее основание, b - верхнее основание, h - высота'''
#     return h * (a+b) / 2

# S = trapezoid_s(4, 6, h=10)
# print(S)
    
# # Произвольное число параметров
# # print(1, 2, 3, 4, 5, 'Hello', []], []])
# def sum_all(*arg):
#     pass
# print(sum_all(1, 2, 3, 4, 5, 100))

# # или

# total = 0
# for i in args:
#         total += i
# return total

# print(sum_all(1, 2, 3, 4, 5, 100))



