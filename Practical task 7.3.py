class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.simbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __add__(self, other):
        return Cell(abs(round(self.cell + other.cell)))

    def __sub__(self, other):
        return Cell(abs(round(self.cell - other.cell)))

    def __mul__(self, other):
        return Cell(abs(round(self.cell * other.cell)))

    def __truediv__(self, other):
        return Cell(abs(round(self.cell // other.cell)))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for i in range(1, count + 1):
                print(self.simbol, end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')


a = Cell(2.3)
b = Cell(5.1)
c = Cell(13.3)
d = Cell(2.7)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)
