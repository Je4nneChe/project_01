# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    pass

# Решение A

# Метод replace() позволяет заменить одни символы в строке на другие.
# В качестве замены может выступать пустая строка, что будет эквивалентно удалению

def remove_exclamation_marks(s):
    return s.replace('!','') 
 
print(remove_exclamation_marks('Hi! Hello!'))
print(remove_exclamation_marks(''))
print(remove_exclamation_marks('Oh, no!!!'))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    pass

# Решение B
# используем цикл if для прохода по символам строки
# присваиваем последнему элементу строки переменную
# проверяем выполнение условия, если да, то отнимаем текущий символ
def remove_last_em(s):
    if s[-1]=='!':
       s=s[:len (s)-1]
    return s

print (remove_last_em('Hi!'))
print (remove_last_em('Hi!!!'))
print (remove_last_em('!Hi'))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass

# Решение


# Подумаю еще)))