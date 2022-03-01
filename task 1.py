class Matrix:
    def __init__(self, data):
        self.mat = data

    def __str__(self):
        lines = ''
        for i in self.mat:
            for j in i:
                lines = lines + '%s\t' % (j)
            lines = lines[:-1]
            lines = lines + '\n'
        lines = lines[:-1]
        return lines

    def __add__(self, other):
        result = []
        num = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summ = other.mat[i][j] + self.mat[i][j]
                num.append(summ)
                if len(num) == len(self.mat[0]):
                    result.append(num)
                    num = []
        return Matrix(result)


a = [[4, 7, 15], [1, 5, 9], [-3, 14, -8]]
b = [[-3, 3, 3], [1, 2, -10], [5, -13, 0]]
mA = Matrix(a)
mB = Matrix(b)

print("\nМатрица 1:")
print(mA.__str__(), "\n")

print("Матрица 2:")
print(mB.__str__(), "\n")

print("Сумма матриц 1 и 2:")
print(mA + mB)