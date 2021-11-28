
from matrix import Matrix, spiral_generator
import unittest as test


class TestMatrix(test.TestCase):
    lhs = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
    rhs = Matrix([9, 8, 7], [6, 5, 4], [3, 2, 1])

    def test_wrong_constructor_parameters(self):
        self.assertRaises(ValueError, Matrix, rows=-1, columns=-2)

    def test_default_matrix(self):
        self.assertEqual(Matrix(rows=2, columns=2), Matrix([0, 0], [0, 0]))

    def test_addition(self):
        self.assertTrue(self.lhs + self.rhs == Matrix([10, 10, 10], [10, 10, 10], [10, 10, 10]))

    def test_wrong_addition(self):
        wrong_matrix = Matrix([1, 2, 3], [4, 5, 6])
        self.assertRaises(ValueError, self.lhs.__add__, wrong_matrix)

    def test_subtraction(self):
        self.assertTrue(self.lhs - self.rhs == Matrix([-8, -6, -4], [-2, 0, 2], [4, 6, 8]))

    def test_multiplication(self):
        self.assertTrue(self.lhs * self.rhs == Matrix([30, 24, 18], [84, 69, 54], [138, 114, 90]))

    def test_item_getter(self):
        right_matrix = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]
        i = 0
        j = 0
        for ii in self.lhs:
            self.assertListEqual(ii.tolist(), right_matrix[i])
            for ji in ii:
                self.assertEqual(ji, right_matrix[i][j])
                j += 1
            i += 1
            j = 0

    def test_wrong_getter(self):
        self.assertRaises(ValueError, self.rhs.__getitem__, 4)

    def test_transposed_matrix(self):
        test_matrix = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
        test_matrix.transpose()
        self.assertTrue(test_matrix == Matrix([1, 4, 7], [2, 5, 8], [3, 6, 9]))

    def test_inverted_matrix(self):
        test_matrix = Matrix([1, 2], [3, 4])
        test_matrix.invert()
        self.assertTrue(test_matrix == Matrix([-2,  1], [1.5, -0.5]))

    def test_linear_equation_solution(self):
        test_matrix = Matrix([9, 6], [10, -6])
        self.assertEqual(test_matrix.solve_linear_equations([15, 4])[0], 1.)
        self.assertEqual(test_matrix.solve_linear_equations([15, 4])[1], 1.)

    def test_wrong_linear_equation_solution(self):
        test_matrix = Matrix([9, 6], [10, -6])
        self.assertRaises(ValueError, test_matrix.solve_linear_equations, vector_b=[15, 4, 3])

    def test_eigenvalue(self):
        self.assertEqual(self.lhs.get_eigenvalue()[0], 16.116843969807032)
        self.assertEqual(self.lhs.get_eigenvalue()[1], -1.1168439698070431)
        self.assertEqual(self.lhs.get_eigenvalue()[2], -3.384336049029656e-16)

    def test_eigenvector(self):
        self.assertEqual(self.lhs.get_eigenvector()[0][0], -0.23197068724628592)
        self.assertEqual(self.lhs.get_eigenvector()[0][1], -0.7858302387420674)
        self.assertEqual(self.lhs.get_eigenvector()[0][2], 0.408248290463863)
        self.assertEqual(self.lhs.get_eigenvector()[1][0], -0.5253220933012335)
        self.assertEqual(self.lhs.get_eigenvector()[1][1], -0.086751339256628)
        self.assertEqual(self.lhs.get_eigenvector()[1][2], -0.8164965809277261)
        self.assertEqual(self.lhs.get_eigenvector()[2][0], -0.8186734993561815)
        self.assertEqual(self.lhs.get_eigenvector()[2][1], 0.6123275602288101)
        self.assertEqual(self.lhs.get_eigenvector()[2][2], 0.40824829046386296)

    def test_norm(self):
        self.assertEqual(self.lhs.get_norm(), 16.881943016134134)

    def test_spiral_generator(self):
        right_spiral_traversal = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        j = 0
        for i in spiral_generator(self.lhs):
            self.assertEqual(i, right_spiral_traversal[j])
            j += 1

    def test_n(self):
        m = Matrix([1,1,1,1,1],
                   [2,2,2,2,2],
                   [3,3,3,3,3],
                   [4,4,4,4,4],
                   [5,5,5,5,5])

        for i in spiral_generator(m):
            print(i)
