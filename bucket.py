# Класс Bucket
# разместить в экземпляре класса Bucket строки, которые имитируют файлы 
# index.html, README.md, page_404.html

# Магические методы Python

class Bucket:
    '''
    Контейнер для хранения объектов облачного сервиса 
    '''
    
    def __init__(self, *, tutorial=None):
        self.content = []
        if tutorial == True:
            self.content.append('README.md')


    def __str__(self):
        return "Содержимое: " + ', '.join(self.content)
    

    def __bool__(self):
        return self.content != []


    def add(self, obj):
        self.content.append(obj)

        


website = Bucket(tutorial=True)
website.add('index.html')
print(website.content)
print(website)

empty_bucket = Bucket()
# print(bool(empty_bucket))
print(bool(website))