import unittest
import numpy as np

class TestNumpyCheatSheet(unittest.TestCase):

    def test_array_creation(self):
        arr = np.array([1, 1.5, 2])
        np.testing.assert_array_equal(arr, np.array([1, 1.5, 2]))

    def test_linspace(self):
        arr = np.linspace(0, 1, 5)
        np.testing.assert_array_equal(arr, np.array([0.0, 0.25, 0.5, 0.75, 1.0]))

    def test_arange(self):
        arr = np.arange(0, 1, 0.25)
        np.testing.assert_array_equal(arr, np.array([0.0, 0.25, 0.5, 0.75]))

    def test_zeros(self):
        arr = np.zeros((3, 4))
        np.testing.assert_array_equal(arr, np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))

    def test_ones(self):
        arr = np.ones((3, 4))
        np.testing.assert_array_equal(arr, np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))

    def test_full(self):
        arr = np.full((3, 4), 2)
        np.testing.assert_array_equal(arr, np.array([[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]))

    def test_eye(self):
        arr = np.eye(3)
        np.testing.assert_array_equal(arr, np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    def test_random(self):
        np.random.seed(0)
        arr = np.random.random((3, 4))
        expected = np.array([[0.5488135, 0.71518937, 0.60276338, 0.54488318],
                             [0.4236548, 0.64589411, 0.43758721, 0.891773],
                             [0.96366276, 0.38344152, 0.79172504, 0.52889492]])
        np.testing.assert_array_almost_equal(arr, expected, decimal=8)

    def test_randint(self):
        np.random.seed(0)
        arr = np.random.randint(10, size=(3, 4))
        expected = np.array([[5, 0, 3, 3], [7, 9, 3, 5], [2, 4, 7, 6]])
        np.testing.assert_array_equal(arr, expected)

    def test_randn(self):
        np.random.seed(0)
        arr = np.random.randn(3, 4)
        expected = np.array([[1.76405235, 0.40015721, 0.97873798, 2.2408932],
                             [1.86755799, -0.97727788, 0.95008842, -0.15135721],
                             [-0.10321885, 0.4105985, 0.14404357, 1.45427351]])
        np.testing.assert_array_almost_equal(arr, expected, decimal=8)

    def test_empty(self):
        arr = np.empty((3, 4))
        self.assertEqual(arr.shape, (3, 4))

    def test_meshgrid(self):
        a = np.array([1, 2])
        b = np.array([3, 4, 5])
        X, Y = np.meshgrid(a, b)
        np.testing.assert_array_equal(X, np.array([[1, 2], [1, 2], [1, 2]]))
        np.testing.assert_array_equal(Y, np.array([[3, 3], [4, 4], [5, 5]]))

    def test_inspect_array(self):
        A = np.random.randn(3, 4)
        self.assertEqual(A.shape, (3, 4))
        self.assertEqual(A.size, 12)
        self.assertEqual(len(A), 3)
        self.assertEqual(A.ndim, 2)
        self.assertEqual(A.dtype, np.float64)

    def test_astype(self):
        x = np.array([1, 2, 2.5])
        np.testing.assert_array_equal(x.astype(int), np.array([1, 2, 2]))

    def test_matrix_multiplication(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        np.testing.assert_array_equal(A @ B, np.array([[19, 22], [43, 50]]))
        np.testing.assert_array_equal(np.matmul(A, B), np.array([[19, 22], [43, 50]]))
        np.testing.assert_array_equal(np.dot(A, B), np.array([[19, 22], [43, 50]]))

    def test_element_wise_operations(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        np.testing.assert_array_equal(A + B, np.array([[6, 8], [10, 12]]))
        np.testing.assert_array_equal(A - B, np.array([[-4, -4], [-4, -4]]))
        np.testing.assert_array_equal(A * B, np.array([[5, 12], [21, 32]]))
        np.testing.assert_array_equal(A / B, np.array([[0.2, 0.33333333], [0.42857143, 0.5]]))
        np.testing.assert_array_equal(A // B, np.array([[0, 0], [0, 0]]))
        np.testing.assert_array_equal(A % B, np.array([[1, 2], [3, 4]]))
        np.testing.assert_array_equal(A ** B, np.array([[1, 64], [2187, 65536]]))
        np.testing.assert_array_equal(A == B, np.array([[False, False], [False, False]]))
        np.testing.assert_array_equal(A != B, np.array([[True, True], [True, True]]))
        np.testing.assert_array_equal(A > B, np.array([[False, False], [False, False]]))
        np.testing.assert_array_equal(A >= B, np.array([[False, False], [False, False]]))
        np.testing.assert_array_equal(A < B, np.array([[True, True], [True, True]]))
        np.testing.assert_array_equal(A <= B, np.array([[True, True], [True, True]]))

    def test_aggregate_operations(self):
        A = np.array([[1, 2], [3, 4]])
        self.assertEqual(A.mean(), 2.5)
        self.assertEqual(A.std(), 1.118033988749895)
        self.assertEqual(np.median(A), 2.5)
        np.testing.assert_array_equal(A.mean(axis=0), np.array([2, 3]))
        np.testing.assert_array_equal(A.std(axis=0), np.array([1, 1]))
        np.testing.assert_array_equal(A.sum(axis=0), np.array([4, 6]))

    def test_corrcoef(self):
        u = np.array([1, 2, 3])
        v = np.array([4, 5, 6])
        np.testing.assert_array_equal(np.corrcoef(u, v), np.array([[1, 1], [1, 1]]))

    def test_any(self):
        arr = np.array([[True, False], [False, False]])
        np.testing.assert_array_equal(np.any(arr, axis=0), np.array([True, False]))

    def test_clip(self):
        a = np.arange(10)
        np.testing.assert_array_equal(np.clip(a, 1, 8), np.array([1, 1, 2, 3, 4, 5, 6, 7, 8, 8]))

if __name__ == '__main__':
    unittest.main()
