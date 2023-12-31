# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!


    # Решение
months = {'1':  "Вы ввели Январь. 31 день",
          '2':  "Вы ввели Февраль. 28 дней",
          '3':  "Вы ввели Март. 31 день",
          '4':  "Вы ввели Апрель. 30 дней",
          '5':  "Вы ввели Май. 31 день",
          '6':  "Вы ввели Июнь. 30 дней",
          '7':  "Вы ввели Июль. 31 день",
          '8':  "Вы ввели Август. 31 день",
          '9':  "Вы ввели Сентябрь. 30 дней",
          '10': "Вы ввели Октябрь. 31 день",
          '11': "Вы ввели Ноябрь. 30 дней",
          '12': "Вы ввели Декабрь. 31 день",
          }
num_month = input('Введите номер месяца: ')
if num_month.isdigit():
   month = int(num_month)

   if 1 <= month <= 12:
       day_count = months[num_month]
       print(day_count)
   else:
       print('Такого месяца нет!')
else:
    print('Необходимо ввести число.')
