import unittest


def spiral_order(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # traverse from left to right
        for i in range(left, right):
            res.append(matrix[top][i])
        print("L->R: ", res)
        top += 1
        # traverse from top to bottom
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        print("T->B: ", res)
        right -= 1

        # recheck conditions
        if not (left < right) or not (top < bottom):
            break

        # traverse from right to left
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        print("R->L: ", res)
        bottom -= 1
        # travese from bottom to top
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        print("B->T: ", res)
        left += 1

    return res


class SpiralMatrixTest(unittest.TestCase):
    def test_spiral_order(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(spiral_order(matrix), expected)
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(spiral_order(matrix), expected)
        # single row matrix
        self.assertEqual(spiral_order([[1, 2, 3]]), [1, 2, 3])
        # single column matrix
        self.assertEqual(spiral_order([[1], [2], [3]]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
