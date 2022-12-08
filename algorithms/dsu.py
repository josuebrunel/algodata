import unittest


class DSU:

    def __init__(self, N):
        self.parents = {i: i for i in range(N)}
        self.ranks = {i: 0 for i in range(N)}

    def find(self, u):
        u = self.parents[u]
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
        return u

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        if self.ranks[u] > self.ranks[v]:
            self.parents[v] = u
        elif self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
        else:
            self.parents[u] = v
            self.ranks[v] += 1
        return True


class DSUTest(unittest.TestCase):

    def test_dsu(self):
        edges = [[1, 2], [4, 1], [2, 4], [2, 3]]
        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            dsu.union(u, v)
        self.assertEqual(dsu.union(4, 1), False)


if __name__ == "__main__":
    unittest.main()
