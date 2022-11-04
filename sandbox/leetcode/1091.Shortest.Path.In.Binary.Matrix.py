import unittest

from collections import deque


def shortestPathBinaryMatrix(grid):
    print(grid)
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] or grid[rows - 1][cols - 1]:
        return -1
    q = deque()
    seen = set((0, 0))
    q.append((0, 0, 1))

    while q:
        for _ in range(len(q)):
            r, c, dist = q.popleft()
            if r == rows - 1 and c == cols - 1:
                return dist

            directions = [[-1, -1], [1, 1], [-1, 1], [1, -1], [0, -1], [0, 1],
                          [-1, 0], [1, 0]]
            for dr, dc in directions:
                if (min(dr + r, dc + c) < 0 or dr + r >= rows or dc + c >= cols
                        or grid[dr + r][dc + c] == 1
                        or (dr + r, dc + c) in seen):
                    continue

                print(
                    f"Follow grid[{dr + r}][{dc + c}] ({grid[dr + r][dc + c]})"
                )
                q.append((dr + r, dc + c, dist + 1))
                seen.add((dr + r, dc + c))

    return -1


class ShortestPathInBinaryMatrix(unittest.TestCase):

    def test_shortest_path_in_binrary_matrix(self):
        self.assertEqual(shortestPathBinaryMatrix([[0, 1], [1, 0]]), 2)
        self.assertEqual(
            shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]), 4)
        self.assertEqual(
            shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]), -1)
        self.assertEqual(
            shortestPathBinaryMatrix([[0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0],
                                      [0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0],
                                      [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0]]),
            14)


if __name__ == "__main__":
    unittest.main()
