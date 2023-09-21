import random
class Matrix:
  def __init__ (self, *, rows: int = 3, colomns: int = 5, value: int | None = None):

    self.rows = rows
    self.colomns = colomns
    self.value = value
    self.data = [[value] * self.colomns for i in range(self.rows)]

  def __str__(self) -> str:
        result = ''
        for row in self.data:
            result += ' '.join([str(elem) for elem in row]) + '\n'
        return result

  def change_all_values(self, new_value: int):
        
        self.data = [[new_value] * self.colomns for i in range(self.rows)]

  def change_element(self, *, colomn: int, row: int, value: int) -> None:
        
        self.data[row][colomn] = value

  def get_measure(self) -> tuple:
        
        return self.rows, self.colomns

  def rundomize_values(self,):
        self.data = [[random.randint(0,9) for _ in range(self.colomns)] for i in range(self.rows)]

if __name__ == '__main__':

    matrix = Matrix(rows=10, colomns=10, value=1)
    print(matrix)

    measure = matrix.get_measure()
    print(f'Размер матрицы:\nкол-во строк - {measure[0]}\nкол-во колонок - {measure[1]}\n')

    matrix.change_element(row=1, colomn=3, value=5)
    print(matrix)

   
    matrix.change_all_values(6)
    print(matrix)

    matrix.rundomize_values()
    print(matrix) 
    