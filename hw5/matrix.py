#!/usr/bin/env python3.6

import random


class Matrix:
    """Class for matrix and operations with them
    """


    def __init__(self, *args):
        """Creates matrix

            :param args: int or list
           :param args: takes number of rows and columns of matrix or a whole matrix
           :raises: TypeError, ValueError
        """

        self.result = []
        if len(args) == 1 and isinstance(args[0], list):
            for el in args[0]:
                if not isinstance(el, list):
                    raise TypeError("Row of matrix must be list")
                if not all(map(lambda x: isinstance(x, int), el)):
                    raise ValueError('Elements of row must be int')
            self.matrix = args[0]
            self.col = len(args[0][0])
            self.row = len(args[0])
        elif len(args) == 2 and all(map(lambda x: isinstance(x, int), args)):
            if any(map(lambda x: x <= 0, args)):
                raise ValueError('Incorrect arguments')
            self.col = args[1]
            self.row = args[0]
            self.matrix = [[random.randint(0, 5) for x in range(self.col)] for v in range(self.row)]
        else:
            raise TypeError('Incorrect arguments')

    def __str__(self):
        """Function to generate view of matrix
        """

        matrix_view = ''
        for i in self.matrix:
            for row in i:
                matrix_view += str(row) + ' '
            matrix_view += ' \n'
        return matrix_view


    def __eq__(self, other):
        """Function that checks wheather matrix are equal

        :param other: two matrixes Matrix type
        :return: bool
        """

        if self.col == other.col and self.row == other.row:
            result = []
            for i in range(self.row):
                for j in range(self.col):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            else:
                return True


    def transposition(self):
        """Transpose matrix

        :return: transposed matrix Matrix type
        """

        return Matrix([[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))])

    def is_squared(self):
        """Checks wheather matrix is squared

        :return: bool
        """

        return self.col == self.row



    def __add__(self, other):
        """Sums two matrix

        :param other: two matrix
        :return: matrix Matrix type
        """
        result = [[0 for x in range(self.col)] for h in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                result[i][j] = self.matrix[i][j]+other.matrix[i][j]
        return Matrix(result)


    def __sub__(self, other):
        """ Substruct two matrix

        :param other: two matrix
        :return: matrix Matrix type
        """
        result = [[0 for x in range(self.col)] for h in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                result[i][j] = self.matrix[i][j]-other.matrix[i][j]
        return Matrix(result)


    def __mul__(self, other):
        """Multiply two matrix

        :param other: two matrix
        :return: matrix Matrix type
        """

        buf = []
        result_matrix = []
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                sums = 0
                for k in range(len(other.matrix)):
                    sums = sums + (self.matrix[i][k] * other.matrix[k][j])
                buf.append(sums)
            result_matrix.append(buf)
            buf = []
        return Matrix(result_matrix)


    def scalar(self, num):
        """Multyply matrix on number

        :param num:
        :return: matrix Matrix type
        :raises: ValueError
        """
        if isinstance(num, int):
            result = [[0 for x in range(self.col)] for h in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] = self.matrix[i][j]*num
            return Matrix(result)
        else:
            raise ValueError('Number is not int')



    def is_symmetric(self):
        """Checks wheather matrix is symmetric

        :return: bool
        :raises: ValueError
        """

        if self.is_squared():
            return self == self.transposition()
        raise ValueError('It is not a squared matrix, sorry')




if __name__ == "__main__":
    a = Matrix(3, 3)
    b = Matrix(3, 6)





