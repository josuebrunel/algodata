import unittest


class DSU:

    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, u):
        u = self.parents[u]
        while u != self.parents[u]:
            u = self.parents[self.parents[u]]
        return u

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        self.parents[u] = v


def is_bipartite(n, dislikes):
    dsu = DSU(2 * (n + 1))

    print(n, dsu.parents)
    for u, v in dislikes:
        dsu.union(u, v + n + 1)
        print(f"U({u, v} with v = {v+n+1} = {dsu.parents}")
        dsu.union(u + n + 1, v)
        print(f"U({u, v} with u = {u+n+1} = {dsu.parents}")

    for i in range(n + 1):
        if dsu.find(i) == dsu.find(i + n + 1):
            return False

    return True


class PossibleBipartionTest(unittest.TestCase):

    def test_is_bipartite(self):
        self.assertEqual(is_bipartite(4, [[1, 2], [1, 3], [2, 4]]), True)
        self.assertEqual(is_bipartite(3, [[1, 2], [1, 3], [2, 3]]), False)
        self.assertEqual(
            is_bipartite(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]), False)


if __name__ == "__main__":
    unittest.main()
