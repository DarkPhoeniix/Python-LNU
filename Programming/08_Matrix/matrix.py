
import numpy as np


class Matrix:
    def __init__(self, *args, rows=1, columns=1):
        if rows <= 0 or columns <= 0:
            raise ValueError('Error matrix size: rows=' + str(rows) + ' columns=' + str(columns))

        self.__num_rows = rows
        self.__num_cols = columns
        self.__index = -1
        if len(args) == 0:
            self.__matrix = np.zeros((rows, columns))
        elif isinstance(args[0], np.ndarray):
            self.__matrix = args[0]
            self.__num_rows = len(args[0])
            self.__num_cols = len(args[0][0])
        else:
            self.__matrix = np.array(args)
            self.__num_rows = len(args)
            self.__num_cols = len(args[0])

    def __add__(self, other):
        self.__check_other_matrix(other, 'add')
        result_matrix = np.add(self.__matrix, other.__matrix)
        return Matrix(result_matrix)

    def __sub__(self, other):
        self.__check_other_matrix(other, 'sub')
        result_matrix = np.subtract(self.__matrix, other.__matrix)
        return Matrix(result_matrix)

    def __mul__(self, other):
        self.__check_other_matrix(other, 'mul')
        result_matrix = np.matmul(self.__matrix, other.__matrix)
        return Matrix(result_matrix)

    def __eq__(self, other):
        return np.allclose(self.__matrix, other.__matrix)

    def __getitem__(self, item: int):
        if item < 0 or item > self.__num_rows:
            raise ValueError('Index out of range: ' + str(item))

        return self.__matrix[item]

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == self.__num_rows:
            self.__index = -1
            raise StopIteration
        return self.__matrix[self.__index]

    def input_matrix(self):
        r, c = map(int, input("Input matrix size (n*m): ").split())
        self.__num_rows = r
        self.__num_cols = c
        matrix = np.array([])
        for i in range(0, r):
            temp_list = list(map(int, input().split()))
            matrix = np.append(matrix, temp_list)
        try:
            self.__matrix = matrix.reshape((r, c))
        except ValueError:
            raise ValueError("Wrong input")

    def __check_other_matrix(self, other, op: str):
        if not isinstance(other, Matrix):
            raise TypeError('Unexpected type while summarizing matrices: ' + type(other))
        elif (op == 'add' or op == 'sub') and \
             (self.__num_rows != other.num_rows or self.__num_cols != other.num_columns):
            raise ValueError('Matrices have different sizes: (' +
                             str(self.__num_rows) + ', ' + str(self.__num_cols) + '), (' +
                             str(other.num_rows) + ', ' + str(other.num_columns) + ')')
        elif op == 'mul' and self.__num_rows != other.num_columns:
            raise ValueError('Matrices have different sizes: (' +
                             str(self.__num_rows) + ', ' + str(self.__num_cols) + '), (' +
                             str(other.num_rows) + ', ' + str(other.num_columns) + ')')

    def transpose(self):
        self.__matrix = self.__matrix.transpose()

    def invert(self):
        self.__matrix = np.linalg.inv(self.__matrix)

    def solve_linear_equations(self, vector_b: []):
        if self.__num_rows != len(vector_b):
            raise ValueError('Wrong sizes: (' +
                             str(self.__num_rows) + ', ' + str(self.__num_cols) + '),' + str(len(vector_b)) + ')')

        return np.linalg.solve(self.__matrix, np.array(vector_b))

    def get_eigenvalue(self):
        return np.linalg.eig(self.__matrix)[0]

    def get_eigenvector(self):
        return np.linalg.eig(self.__matrix)[1]

    def get_norm(self):
        return np.linalg.norm(self.__matrix)

    @property
    def num_rows(self):
        return self.__num_rows

    @property
    def num_columns(self):
        return self.__num_cols


def spiral_generator(matrix):
    elements = matrix.num_rows * matrix.num_columns
    rows = matrix.num_rows
    cols = matrix.num_columns
    i = 0
    j = 0
    step = 0
    while elements > 0:
        while j < cols + step and elements != 0:
            yield matrix[i][j]
            elements -= 1
            j += 1
        cols -= 1
        i += 1
        j -= 1

        while i < rows + step and elements != 0:
            yield matrix[i][j]
            elements -= 1
            i += 1
        rows -= 1
        j -= 1
        i -= 1

        while j >= 0 and elements != 0:
            yield matrix[i][j]
            elements -= 1
            j -= 1
        j += 1
        cols -= 1
        i -= 1

        while i > 0 and elements != 0:
            yield matrix[i][j]
            elements -= 1
            i -= 1
        step += 1
        i += step
        rows -= 1
        j += 1
