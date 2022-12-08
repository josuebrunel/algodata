import unittest


def find_redundant_connection(edges):
    parent = {i: i for i in range(len(edges) + 1)}
    rank = {i: 0 for i in range(len(edges) + 1)}

    def find(u):
        u = parent[u]
        while u != parent[u]:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u, v = find(u), find(v)
        if u == v:
            return False

        if rank[u] > rank[v]:
            parent[v] = u
        elif rank[u] < rank[v]:
            parent[u] = v
        else:
            parent[u] = v
            rank[v] += 1
        return True

    res = None
    for u, v in edges:
        if not union(u, v):
            res = (u, v)

    return res


class RedundantConnectionTest(unittest.TestCase):

    def test_redundant_connection(self):
        self.assertCountEqual(
            find_redundant_connection([[1, 2], [1, 3], [2, 3]]), [2, 3])
        self.assertCountEqual(
            find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4],
                                       [1, 5]]), [1, 4])


if __name__ == "__main__":
    unittest.main()
