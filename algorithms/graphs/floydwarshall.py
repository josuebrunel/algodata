import unittest


def floyd_warshall(n, edges):
    distances = [[float("inf")] * n for i in range(n)]
    for i in range(n):
        distances[i][i] = 0

    for u, v, w in edges:
        distances[u - 1][v - 1] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j],
                                      distances[i][k] + distances[k][j])
    return distances


class FloydWarshall(unittest.TestCase):

    def test_floyd_warshall(self):
        edges = [[1, 3, -2], [3, 4, 2], [4, 2, -1], [2, 3, 3], [2, 1, 4]]
        result = [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
        self.assertCountEqual(floyd_warshall(4, edges), result)
        edges = [[1, 2, 3], [2, 1, 8], [2, 3, 2], [3, 1, 5], [3, 4, 1],
                 [4, 1, 2], [1, 4, 7]]
        result = [[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]
        self.assertCountEqual(floyd_warshall(4, edges), result)


if __name__ == "__main__":
    unittest.main()
