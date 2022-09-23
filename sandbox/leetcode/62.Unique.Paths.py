import unittest


# O(m*n) time | O(m*n) space
def unique_paths(m, n):
    grid = [[1 for j in range(n)] for i in range(m)]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
    print(grid)
    return grid[m - 1][n - 1]


class UniquePathsTest(unittest.TestCase):

    def test_unique_paths(self):
        self.assertEqual(unique_paths(3, 7), 28)
        self.assertEqual(unique_paths(3, 2), 3)


if __name__ == "__main__":
    unittest.main()
