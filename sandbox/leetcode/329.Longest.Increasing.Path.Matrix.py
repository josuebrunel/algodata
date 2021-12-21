import unittest


def longestIncreasingPath(matrix):
    lip = [[0 for _ in i] for i in matrix]
    prev = -1
    max_lip = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            max_lip = max(max_lip, dfs(i, j, matrix, lip, prev))
    return max_lip


def dfs(i, j, matrix, lip, prev):
    # if current less than prev return 0
    if matrix[i][j] <= prev:
        return 0
    # if current greater than 0, it means its lip is already computed
    if lip[i][j] > 0:
        return lip[i][j]
    # computed current lip
    cur_lip = 1
    neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for n in neighbors:
        x = n[0] + i
        y = n[1] + j
        if not (0 <= x < len(matrix)):
            continue
        if not (0 <= y < len(matrix[i])):
            continue

        cur_lip = max(cur_lip, 1 + dfs(x, y, matrix, lip, matrix[i][j]))
    lip[i][j] = cur_lip
    print(i, j, cur_lip)
    return cur_lip


class TestLongestIncreasingPath(unittest.TestCase):
    def test_longest_increasing_path(self):
        self.assertEqual(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)
        self.assertEqual(longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]), 4)
        self.assertEqual(longestIncreasingPath([[7, 7, 5], [2, 4, 6], [8, 2, 0]]), 4)


if __name__ == "__main__":
    unittest.main()
