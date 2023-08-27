# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    pass

def maximum(arr):
    pass


# Решение
# Исходный список чисел
numbers = [22, 44, 77, 33, 55, 8, 99]

# Инициализация переменных max_number и min_number
max_number, min_number = numbers[0], numbers[0]

# Цикл for для прохода по всем элементам списка
for number in numbers:
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number  

print('min =', min_number, ',', 'max =', max_number)