import unittest


# O(v*E)
def bellman_ford(n, edges, src):
    """The idea is to compute the shortest
    for N-1 times. At each iteration:
    - if src weight is infinity, we skip
    - if src weight + dst weight < temporary dst weight
    we update temporary dst weight
    - after each iteration, temporary weights holder become
    original weights
    - to validate the result we should one more iteration
    and make sure that values haven't changes. If values
    changes after N iteration it means that we have a
    negative weight cycle
    """
    inf = float("inf")
    adj = {}
    for s, d, _ in edges:
        adj[s] = inf
        adj[d] = inf

    adj[src] = 0

    for _ in range(n):
        tmp = adj.copy()
        for s, d, w in edges:
            if adj[s] == inf:
                continue
            if adj[s] + w < tmp[d]:
                tmp[d] = tmp[s] + w
            print(adj, tmp)

        adj = tmp

    return adj.values()


class BellmanFordTest(unittest.TestCase):

    def test_bellman_ford(self):
        edges = [["S", "A", 10], ["S", "E", 8], ["E", "D", 1], ["D", "A", -4],
                 ["D", "C", -1], ["A", "C", 2], ["C", "B", -2], ["B", "A", 1]]
        self.assertCountEqual(bellman_ford(6, edges, "S"), [0, 5, 5, 7, 9, 8])


if __name__ == "__main__":
    unittest.main()
