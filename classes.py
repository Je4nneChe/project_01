# Классы в Python

# Императивный стиль - запись четких инструкций для выполнения
# Объектно-ориенторованное программирование - создание объектов и описание 


# какие объекты можно выделить в социальной сети?
# 1. Экран входа - объекты: Пользователь - атрибуты: логин, пароль
# 2. Главная лента - объекты: пост - атрибуты: содержание, время публ-ции, лайки 

# другой объект - метод: выложить пост


# КЛАСС ОБЪЕКТА -???
# этап создания класса
# имена классов записывать с большой буквы каждое новое слово (CamelClass)
class Cell:
    content = 1
    content_type = type(content)

    def add(self, obj):
        self.content = obj
        self.content_type = type(obj)

# Создание экземпляра класса
A1 = Cell()
A1.add(100)
print(A1.content, A1.content_type)



class Row:
    def __init__(self, *args):
        self.args = args
    
    def __eq__(self, other):
        return self.args + other.args

    def __hash__(self) -> int:
        return hash(self.args)
    
    
    def __add__(self, other):
        return self.args + other.args if isinstance(other, Row) else self.args + other

r1 = Row(1, 2, 3)
r2 = Row(1, 2, 3)    

print(r1 == r2)
print(r1 + r2)
print(r1 + (1, 2))

print({r1: 'vef', r2: 'cwdcwe'})



## Что такое класс объекта - это шаблон, по которому создаются новые объекты
# разберем пример на ммашинах

class Car:
    #  атрибут - переменные внутри
    color = 'Black'
    wheels = 4
    engine_status = False

    # методы - функции внутри класса
    # связанный метод класса
    def horn(self):
        print('beeb!')

    def start_engine(self, key):
        if key == 'Ключ':
            self.engine_status = True
            return self.engine_status

# Что такое экземпляр класса - это объект, созданный по классу
toyota1 = Car() 
toyota2 = Car() 
toyota3 = Car() 
toyota4 = Car() 


# изменение атрибута экземпляра
toyota1.color = 'Red'
print(toyota1)
print(toyota2)

# Вызов метода экземпляра
toyota1.horn() # TypeError: Car.horn() takes 0 positional arguments but 1 was given - если не  self
print(toyota1.start_engine('Ключ'))
print(toyota1.engine_status)
print(toyota2.engine_status)


# О методе __del__

class Truck: 

    def __init__(self, *args):
        print('Загружено в ковш:')
        [print(f'    *{i}') for i in args]

    def __del__(self):
        print('Содержание выгружено из ковша')

belaz = Truck('песок', 'щебень', 'арматура')


print(2 + 2)


