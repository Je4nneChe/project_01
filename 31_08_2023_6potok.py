# -*- coding: utf-8 -*-
"""31_08_2023_6potok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KtbzePP3A3ad8mZZpvfHby2kL0u-13kI
"""

# Бинарный поиск
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


# Тестовый список и значение
testarr = [6, 15, 17, 18, 52, 59, 65, 70, 94, 96]
val = int(input('Vvedi zna4: '))


# Интерпретация результата
if binary_search(testarr,val) != -1:
  print ('Элемент найден под индексом ',binary_search(testarr,val))
else:
  print ('Элемент не найден в списке')

# Экспоненциальный поиск по сути такой жже, как бинарны
# Экспоненциальный поиск — известный под названиями galloping search, doubling search и Struzik
# search
# ➢ Определяется диапазон, в котором, скорее всего, будет находиться искомый элемент
# ➢ В этом диапазоне используется двоичный поиск (Бинарный поиск) для нахождения индекса
# элемента
# Экспоненциальный поиск работает лучше, чем бинарный, когда искомый элемент находится
# ближе к началу массива.

# Эксопненциальный поиск
def exponential_search(arr,x):
  if arr[0] == x:
    return 0
  index = 1
  while index < len(arr) and arr[index] <= x:
    index = index * 2
  print (arr[:min(index, len(arr))])
  return binary_search(arr[:min(index, len(arr))],x)



# Бинарный поиск
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

# Тестовый список и значение
testarr = [6, 15, 17, 18, 52, 59, 65, 70, 94, 96]
val = int(input('Vvedi zna4: '))


# Интерпретация результата
if exponential_search(testarr,val) != -1:
  print ('Элемент найден под индексом ',exponential_search(testarr,val))
else:
  print ('Элемент не найден в списке')

import math
# Jump поиск
def jump_search(arr,x):
  lenght = len(arr)
  jump = int(math.sqrt(lenght))
  print ('размер прыжка', jump)
  left = 0
  right = 0
  while left < lenght and arr[left] <= x:
    right = min(lenght - 1, left + jump)
    if arr[left] <= x and arr[right] >= x:
      break
    left += jump
  if left >= lenght or arr[left] > x:
    return -1
  right = min(lenght - 1, right)
  i = left
  print (left, right)
  while i <= right and arr[i] <= x:
    print (i)
    if arr[i] == x:
      return i
    i += 1
  return -1



# Тестовый список и значение
testarr = [6, 15, 17, 18, 52, 59, 65, 70, 94, 96]
val = int(input('Vvedi zna4: '))


# Интерпретация результата
if jump_search(testarr,val) != -1:
  print ('Элемент найден под индексом ',jump_search(testarr,val))
else:
  print ('Элемент не найден в списке')

# Интерполяционный поиск
def interpolation_serch(arr,x):
  low = 0
  high = (len(arr) - 1)
  while low <= high and x >= arr[low] and x <= arr[high]:
    index = low + (((x - arr[low]) * (high-low)) // (arr[high] - arr[low]))
    if arr[index] == x:
      return index
    if arr[index] < x:
      low = index + 1
    else:
      high = index - 1
  return - 1



# Тестовый список и значение
testarr = [6, 15, 17, 18, 52, 59, 65, 70, 94, 96]
val = int(input('Vvedi zna4: '))


# Интерпретация результата
if interpolation_serch(testarr,val) != -1:
  print ('Элемент найден под индексом ',interpolation_serch(testarr,val))
else:
  print ('Элемент не найден в списке')

# Бинарный поиск через рекурсию

def binar(arr, low, high, x):
  # Проверка середины
  if high >= low:
    mid = (high + low) // 2
    print (mid)
    # Если элемент в середине
    if arr[mid] == x:
      return mid
    # Если в левой
    elif arr[mid] > x:
      return binar(arr, low, mid - 1, x)
    # Если в правой
    else:
      return binar(arr, mid + 1, high, x)
  else:
    return -1



# Тестовый список и значение
testarr = [6, 15, 17, 18, 52, 59, 65, 70, 94, 96]
val = int(input('Vvedi zna4: '))


# Интерпретация результата
resultat = binar(testarr,0,len(testarr) - 1, val)
if resultat != -1:
  print ('Элемент найден под индексом ', str(resultat))
else:
  print ('Элемент не найден в списке')

x = 3
y = 4

def test():
  yield x + y
  yield x - y

test()

for i in test():
  print (i)

# Задача 3
import os

def get_paths(path = '.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path,name))
    yield abs_path
    if os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)


for i in get_paths('test'):
  print (i)

# Задача 4

import os

def get_paths(path = '.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path,name))
    if os.path.isfile(abs_path) is True:
      yield abs_path
    elif os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)



for i in get_paths('test'):
  print (i)