# КАЛЬКУЛЯТОР
# Написать программу, которая выполняет с дробными числами одну из четырех операций (сложение, вычитание,
# умножение или деление). Программа должна завершаться только по желанию пользователя.
# Чтобы программа самопроизвольно не завершалась, в ней надо запустить бесконечный цикл. Выход из него
# будем осуществлять с помощью оператора break, если пользователь вводит определенный символ вместо знака
# арифметической операции.
# Если пользователь ввел знак, который не является ни знаком арифметической операции, ни символом-
# "прерывателем" работы программы, то вывести сообщение о некорректном вводе.
# Если был введен один из четырех знаков операции, запросить ввод двух чисел.
# В зависимости от знака операции выполнить соответствующее арифметическое действие.
# Если было выбрано деление, необходимо проверить не является ли нулем второе число. Если это так, то
# сообщить о невозможности деления.

# Конструкция match case
print ("Буква q  - выход")
while True:
  s = input('Sign (+,-,*,/):')
  if s == 'q':
    break
  if s in ('+','-','*','/'):
    x = float(input('x = '))
    y = float(input('y = '))
    if s == '+':
      print(x+y)
    elif s == '-':
      print(x-y)
    elif s == '*':
      print (x*y)
    elif s == '/':
      if y != 0:
        print (x/y)
      else:
        print ('delenie na 0')
  else:
    print ('ne korrektny znak')

print ("Буква q  - выход")
while True:
  s = input('Sign (+,-,*,/):')
  match s:
    case 'q':
      break
    case '+':
      x = float(input('x = '))
      y = float(input('y = '))
      print(x+y)
    case '-':
      x = float(input('x = '))
      y = float(input('y = '))
      print(x-y)
    case '*':
      x = float(input('x = '))
      y = float(input('y = '))
      print(x*y)
    case '/':
      x = float(input('x = '))
      y = float(input('y = '))
      if y != 0:
        print (x/y)
      else:
        print ('delenie na 0')
    case _:
      print ('ne korrektny znak')


# Конструкция try except else finally
x = 10
y = 0

try:
    print (x/y)
except ZeroDivisionError:
        print ('delenie na 0')
else:
    print ('block else')

x = 10
e = 2
try:
    print (x/y)
except ZeroDivisionError:
        print ('delenie na 0')
finally:
    print ('block finally')

# ГЕНЕРАТОРЫ СЛУЧАЙНЫХ ЧИСЕЛ
# Задача: Выбрать случайное значение x в интервале от 0 до 100
# Решение:
import random
x = random.randint (10,50)
print (x)

# ВЫБОР СЛУЧАЙНЫХ ЗНАЧЕНИЙ ИЗ СПИСКА

# Задача: Выбрать случайное значение x из списка [0, 10, 25, 40, 100]
# Решение:
import random
x = [0, 10, 25, 40, 100]
print ("Случайное число из списка", random.choice(x))
# Метод choice выбирает случайное значение из списка
# Данный метод также применим и к текстовым значениям и к текстовым переменным
x = [0, 10, 25, 40, 100, 'test', 'test2', [4,5]]

# ИНЫЕ ТИПЫ ГЕНЕРАТОРОВ
# Генератор float на отрезке [0, 1)
x = random.random()
# Генератор float на отрезке со значениями float
x = random.uniform(0.2, 7.5)
print

# ЗАДАЧА 1 
# Написать алгоритм, где игральный кубик (6 сторонний)
# бросается 4 раза.
# Вывести в результаты каждое выпавшее значение.
# Найти сумму выпавших значений.
# Задача 1 var 1

# variant 1
import random
b1 = random.randint(1,6)
print (b1)
b2 = random.randint(1,6)
print (b2)
b3 = random.randint(1,6)
print (b3)
b4 = random.randint(1,6)
print (b4)
total = b1 + b2 + b3 + b4
print ('Itog', total)

# variant 2
import random

k = 4
y = []
total = 0

while k != 0:
  x = random.randint(1,6)
  k -= 1
  y.append(x)
  print (y)

for i in y:
  print ('i = ', i)
  total += i
  print ('total = ', total)

print ('Itog', total)

 
# Задача 2 var 1
# Написать алгоритм генератора случайных паролей из
# следующих символов:
# +-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
# Программа должна запрашивать длину необходимого пароля,
# в случае если в поле для задания длинны вносится не числовое
# значение пользователь должен информироваться о том, что он
# допустил ошибку

# Задача 2
import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = input('Длина пароля: ')
password = ''

try:
  length = int(length)
  for n in range(length):
    password += random.choice(chars)
  print (password)
except ValueError:
  print ('Вы ввели буквы, пожалуйста введите цифры')
finally:
  password = ''
  length = input('Длина пароля: ')
  length = int(length)
  for n in range(length):
    password += random.choice(chars)
  print (password)


# АЛГОРИТМ ЕВКЛИДА
# Алгоритм Евклида – это алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел.
# Наибольший общий делитель (НОД) – это число, которое делит без остатка два числа и делится
# само без остатка на любой другой делитель данных двух чисел. Иными словами, это самое большое
# число, на которое можно без остатка разделить два числа, для которых ищется НОД.
# 1. Делим большее на меньшее, если получается остаток 0, то значит, что числа равны друг другу и
# являются НОД (следует выйти из цикла).
# 2. Если результат вычитания не равен 0, то большее число заменяем на результат вычитания.
# 3. Переходим к пункту 1.
# 4. Из большего числа вычитаем меньшее.
# Алгоритм нахождения НОД делением
# Пример: Найти НОД для чисел 35 и 14
# 35 / 14 = 2 (остаток 7)
# 14 / 7 = 2 (остаток 0)
# Конец НОД это делитель 7.
# НОД (35, 14) = 7

a = 35
b = 14

while a != 0 and b != 0:
  print (a,b)
  if a > b:
    a = a % b
    print ('a = ', a)
  else:
    b = b % a
    print ('b = ', b)

print (a+b)

a = 35
b = 14

while a != b:
  print(a,b)
  if a > b:
    a = a - b
    print ('a = ', a)
  else:
    b = b - a
    print ('b = ', b)

print (b)


#  СОРТИРОВКА ВЫБОРОМ
#  Алгоритм сортировки выбором заключается в поиске на необработанном срезе массива или списка
# минимального значения и в дальнейшем обмене этого значения с первым элементом необработанного
# среза. На следующем шаге необработанный срез уменьшается на один элемент.
# 1. Найти наименьшее значение в списке.
# 2. Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
# 3. Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
# 4. Второй минимум поместить на второе место списка. Второй элемент при этом перемещается на
# освободившееся место.
# 5. Продолжать выполнять поиск и обмен, пока не будет достигнут конец списка.    
l = [10, 7 , 5 ,4] # ставим 4 на место нулевого, потом 5, на место впервого индекса и т.д.
# пример через функцию

# ЗАДАЧА 3
# Отсортировать массив (список)
# [12, 4, 54, 29, 46, 36, 72, 99, 85]
# Вывести итог на экран

from random import randint

n = 10
data = []
for i in range(n):
  data.append(randint(1,99))
print (data)
# дальше пишем алгоритм:

def vibor(lst):         
  n = len(lst)          # уточняем количество элементов в массиве
  i = 0                 # переменная с которой открываем список
  while i < n - 1:      #открыли список
    m = 1               # переменная внутри цикла                 
    j = i + 1
    while  j < n:
      if lst[j] < lst [m]:
        m = j             # переназначим переменную 
      j += 1
    lst[i],lst[m] = lst[m],lst[i]
    i += 1
  return lst

vibor(data)
# на выходе неотсортированный список и отсортированный




# СОРТИРОВКА ПУЗЫРЬКОМ
# Сортировка пузырьком - это метод сортировки массивов и списков путем последовательного сравнения и обмена
# соседних элементов, если предшествующий оказывается больше последующего.
# В процессе выполнения данного алгоритма элементы с большими значениями оказываются в конце списка, а
# элементы с меньшими значениями постепенно перемещаются по направлению к началу списка. Образно говоря,
# тяжелые элементы падают на дно, а легкие медленно всплывают подобно пузырькам воздуха.
# В сортировке методом пузырька количество итераций внешнего цикла определяется длинной списка минус
# единица, так как когда второй элемент становится на свое место, то первый уже однозначно минимальный и
# находится на своем месте.
# Количество итераций внутреннего цикла зависит от номера итерации внешнего цикла, так как конец списка уже
# отсортирован, и выполнять проход по этим элементам смысла нет.

# Дан массив: [7, 13, 5, 3, 9]
# За первую итерацию внешнего цикла число 13 переместится в конец. Для этого потребуется 5 сравнениQ во
# внутреннем цикле:
7 > 13 # ? Нет
13 > 5 # ? Да. Меняем местами
13 > 3 # ? Да. Меняем местами
13 > 9 # ? Да. Меняем местами
print([7, 5, 3, 9, 13])
7 > 5 # ? Да. Меняем местами
7 > 3 # ? Да. Меняем местами
7 > 9 # ? Нет
print([5, 3, 7, 9, 13])
# И так далее, до конца списка…

# Сортировка пузырьком через for
from random import randint

n = 10
data = []
for i in range(n):
  data.append(randint(1,99))
print (data)

def bubble_for(lst):
  n = len(lst)
  for i in range(n - 1):
    for j in range (n - i - 1):
      if lst[j] > lst[j + 1]:       #если элемент с индексом j > элемента с индексом
        lst[j],lst[j+1] = lst[j+1],lst[j]
  return lst

bubble_for(data)


# СОРТИРОВКА ПУЗЫРЬКОМ ЧЕРЕЗ WHILE:

from random import randint

n = 10
data = []
for i in range(n):
  data.append(randint(1,99))
print (data)

def bubble_while(lst):
  n = len(lst)
  i = 0
  while i < n - 1:
    j = 0
    while j < n - i - 1:
      if lst[j] > lst[j+1]:
        lst[j],lst[j+1] = lst[j+1],lst[j]
      j += 1
    i += 1
  return lst

bubble_while(data)

# на выходе неотсортипрованный и отсортированный списки


# Задача 4
# Отсортировать рандомный целочисленный массив из 10 чисел в интервале от (1; 100)
# Любым из пройденных способов

# Бинарный поиск
# Бинарный поиск работает по принципу «разделяй и властвуй». Он быстрее, чем линейный поиск, но требует, чтобы
# массив был отсортирован перед выполнением алгоритма.
# [2, 15, 23, 35, 43, 56, 68, 70, 82, 89]
# Представим себе массив, и представим что мы хотим найти число 70
# Алгоритм делит массив по полам, и сравнивает искомое число со значением числа из середины массива, если число
# равно то алгоритм прекращает свою работу, если оно меньше искомого числа, то алгоритм отбрасывает ту часть
# массива, которая меньше среднего числа (аналогично с большей частью). Далее алгоритм проводит следующие
# подобные итерации с оставшимися частями массива.
# 0 1 2 3 4 5 6 7 8 9
#                 70
# [2, 15, 23, 35, 43, 56, 68, 70, 82, 89]
#  0   1   2   3   4   5   6   7   8   9


# СТАНДАРТНАЯ СОРТИРОВКА

from random import randint

n = 10
data = []
for i in range(n):
  data.append(randint(1,99))
print (data)

def default(lst):
  lst.sort()
  return lst

default(data)

# СОРТИРОВКА ВСТАВКОЙ
from random import randint

n = 10
data = []
for i in range(n):
  data.append(randint(1,99))
print (data)


def insrtion(lst):
  for i in range(len(lst)):
    j = i - 1
    key = lst[i]
    while lst[j] > key and j >= 0:
      lst[j + 1] = lst[j]
      j -= 1
    lst[j + 1] = key
  return lst

insrtion(data)

####### ЗАДАЧА task_2.1 из Домашних работ#######

from datetime import datetime

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]

def vibor(lst):
  n = len(lst)
  i = 0
  while i < n - 1:
    m = i
    j = i + 1
    while  j < n:
      if lst[j] < lst [m]:
        m = j
      j += 1
    lst[i],lst[m] = lst[m],lst[i]
    i += 1
  return lst

def bubble_for(lst):
  n = len(lst)
  for i in range(n - 1):
    for j in range (n - i - 1):
      if lst[j] > lst[j + 1]:
        lst[j],lst[j+1] = lst[j+1],lst[j]
  return lst

def bubble_while(lst):
  n = len(lst)
  i = 0
  while i < n - 1:
    j = 0
    while j < n - i - 1:
      if lst[j] > lst[j+1]:
        lst[j],lst[j+1] = lst[j+1],lst[j]
      j += 1
    i += 1
  return lst

def default(lst):
  lst.sort()
  return lst

def minimum(arr):
    print ('МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ')
    print ('Сортировка выбором')
    start_time = datetime.now()
    for lst in arr:
      print ('Минимальное значение из списка', lst, vibor(lst)[0])
    end_time = datetime.now()
    print ('Продолжительность: {}'.format(end_time - start_time))

    print ('Сортировка пузрьком через for')
    start_time = datetime.now()
    for lst in arr:
      print ('Минимальное значение из списка', lst,bubble_for(lst)[0])
    end_time = datetime.now()
    print ('Продолжительность: {}'.format(end_time - start_time))

    print ('Сортировка пузрьком через while')
    start_time = datetime.now()
    for lst in arr:
      print ('Минимальное значение из списка', lst,bubble_while(lst)[0])
    end_time = datetime.now()
    print ('Продолжительность: {}'.format(end_time - start_time))

    print ('Стандартная сортировка')
    start_time = datetime.now()
    for lst in arr:
      print ('Минимальное значение из списка', lst,default(lst)[0])
    end_time = datetime.now()
    print ('Продолжительность: {}'.format(end_time - start_time))

def maximum(arr):
    print ('МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ')
    print ('Сортировка выбором')
    start_time = datetime.now()
    for lst in arr:
      print ('Максимальное значение из списка', lst,vibor(lst)[-1])
    end_time = datetime.now()
    print ('Продолжительность: {}'.format(end_time - start_time))

    print ('Сортировка пузрьком через for')
    start_time = datetime.now()
    for lst in arr:
      print ('Максимальное значение из списка', lst,bubble_for(lst)[-1])
    end_time = datetime.now()
    print ('Продолжительность: {}'.format(end_time - start_time))

    print ('Сортировка пузрьком через while')
    start_time = datetime.now()
    for lst in arr:
      print ('Максимальное значение из списка', lst,bubble_while(lst)[-1])
    end_time = datetime.now()
    print ('Продолжительность: {}'.format(end_time - start_time))

    print ('Стандартная сортировка')
    start_time = datetime.now()
    for lst in arr:
      print ('Максимальное значение из списка', lst,default(lst)[-1])
    end_time = datetime.now()
    print ('Продолжительность: {}'.format(end_time - start_time))

def main():
  print (minimum(arr))
  print (maximum(arr))

main()

# БИНАРНЫЙ ПОИСК
def binary_search(arr,x):
  low = 0
  high = len(arr)-1
  index = -1
  while (low <= high) and (index == -1):
    mid = (low + high) // 2
    if arr[mid] == x:
      index = mid
    else:
      if x < arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
  return index


# ТЕСТОВЫЙ СПИСОК И ЗНАЧЕНИЕ
testarr = [6, 15, 17, 18, 52, 59, 65, 70, 94, 96]
val = int(input('Vvedi zna4: '))


# ИНТЕРПРЕТАЦИЯ РЕЗУЛЬТАТА
if binary_search(testarr,val) != -1:
  print ('Элемент найден под индексом ',binary_search(testarr,val))
else:
  print ('Элемент не найден в списке')
