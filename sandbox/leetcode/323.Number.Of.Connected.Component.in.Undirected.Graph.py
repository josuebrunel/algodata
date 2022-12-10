import unittest


class DSU:

    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.ranks = {i: 0 for i in range(n)}

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


def connected_components(n, edges):
    dsu = DSU(n)
    res = set()
    for u, v in edges:
        dsu.union(u, v)
    for v in dsu.parents.values():
        res.add(v)
    return len(res)


class NumberOfConnectedComponentsTest(unittest.TestCase):

    def test_conneted_components(self):
        self.assertEqual(connected_components(5, [[0, 1], [1, 2], [3, 4]]), 2)
        self.assertEqual(
            connected_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)


if __name__ == "__main__":
    unittest.main()
