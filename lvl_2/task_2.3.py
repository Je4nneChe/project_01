# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    pass

# Решение
number = int(input('Введите номер: '))
def switch_it_up(number):
  numbers_in_words = {
            1:'one',
            2:'two', 
            3:'three', 
            4:'four', 
            5:'five', 
            6:'six', 
            7:'seven',
            8:'eight', 
            9:'nine', 
            0:'zero'  
    }
  return numbers_in_words.get(number)
result = switch_it_up(number)
print(result)