import unittest
from collections import deque


def display(grid):
    for i in grid:
        print(i)


def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    time, fresh = 0, 0
    # let's count the number of fresh and rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()

            for dr, dc in directions:
                if (not (0 <= dr + r < rows) or not (0 <= dc + c < cols)
                        or grid[dr + r][dc + c] != 1):
                    continue

                print(f"Rot {dr + r, dc + c}")
                q.append((dr + r, dc + c))
                grid[dr + r][dc + c] = 2
                fresh -= 1

        time += 1

    return time if fresh == 0 else -1


class RottenOrangesTest(unittest.TestCase):

    def test_rotten_oranges(self):
        self.assertEqual(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
        self.assertEqual(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)
        self.assertEqual(orangesRotting([[0, 2]]), 0)
        self.assertEqual(orangesRotting([[0, 1]]), -1)


if __name__ == "__main__":
    unittest.main()
