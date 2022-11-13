import unittest


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid
    return -1


def binary_search_matrix(matrix, target):
    row, col = 0, len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if target > matrix[row][col]:
            row += 1
        elif target < matrix[row][col]:
            col -= 1
        else:
            return True

    return False


class BinaraySearchTest(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(binary_search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_binary_search_matrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertIs(binary_search_matrix(matrix, 3), True)
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertIs(binary_search_matrix(matrix, 13), False)


if __name__ == "__main__":
    unittest.main()
