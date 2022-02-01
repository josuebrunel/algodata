import unittest


def max_area_island(grid):
    maxArea = 0
    visited = [[0 for j in i] for i in grid]

    def dfs(i, j):
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])):
            return 0
        if grid[i][j] == 0:
            return 0
        if visited[i][j] != 0:  # if visited or visiting
            return 0

        visited[i][j] = -1  # visiting
        area = 1 + dfs(i, j - 1) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i + 1, j)
        visited[i][j] = 1  # visited
        return area

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            area = dfs(i, j)
            maxArea = max(maxArea, area)

    return maxArea


class MaxAreadIslandTest(unittest.TestCase):
    def test_max_area_island(self):
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        res = 6
        self.assertEqual(max_area_island(grid), res)
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        res = 0
        self.assertEqual(max_area_island(grid), res)


if __name__ == "__main__":
    unittest.main()
