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

# def minimum(arr):
#     pass

# def maximum(arr):
#     pass

# Решение с помощью сортировки пузырьком через for:

arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]
def bubble_for(lst):
  n = len(lst)
  for i in range(n - 1):
    for j in range (n - i - 1):
      if lst[j] > lst[j + 1]:
        lst[j],lst[j+1] = lst[j+1],lst[j]
  return lst
for lst in arr:
  print ('*', lst,'-> min =',bubble_for(lst)[0],', max =',bubble_for(lst)[-1] )

# # Решение для одного списка:
# # Вариант 1
# arr =  [22, 44, 77, 33, 55, 8, 99]
# def maximum(arr):
#     max_num = arr[0]
#     for num in arr:
#         if num > max_num:
#             max_num = num
#     return max_num
# def minimum(arr):
#     min_num = arr[0]
#     for num in arr:
#         if num < min_num:
#             min_num = num
#     return min_num
# print("max =", maximum(arr), ", min =", minimum(arr))


# # Вариант 2
# # Инициализация переменных max_number и min_number
# # Цикл for для прохода по всем элементам списка

# numbers = [22, 44, 77, 33, 55, 8, 99]
# max_number, min_number = numbers[0], numbers[0]
# for number in numbers:
#     if number > max_number:
#         max_number = number 
#     if number < min_number:
#         min_number = number
     
# print('max =', max_number, ',', 'min =', min_number)