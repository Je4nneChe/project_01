# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

# Решение

import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
r3_songs = random.sample(my_favorite_songs, 3)
r3_time = (r3_songs[0][1] + r3_songs[1][1] + r3_songs[2][1])

print('Три песни звучат', int(r3_time), 'минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Решение

time_songs = list(my_favorite_songs_dict.values()) # используем метод словарей Values, чтобы вытащить Значения
r3_time = random.sample(list(time_songs), 3)

print('Три песни звучат', int(sum(r3_time)), 'минут')



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Решение выполняется через модуль datetime метод time()
# 0 <= hour < 24
# 0 <= minute < 60
# 0 <= second < 60
# 0 <= microsecond < 1000000
# fold in [0, 1]

import datetime
time = datetime.time(0,11,22)
print(time, type(time))


