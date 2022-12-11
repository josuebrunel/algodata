import unittest
import collections
import heapq


def djikstra(edges):
    adj = collections.defaultdict(list)
    for src, dst, wgh in edges:
        adj[src].append((dst, wgh))
        adj[dst] = adj.get(dst, [])

    visited = set()
    heap = []
    heapq.heappush(heap, (0, 0))
    shortest = [float("inf")] * len(adj)

    while heap:
        weight, edge = heapq.heappop(heap)
        if edge in visited:
            continue

        visited.add(edge)
        for ne, nw in adj[edge]:
            if ne in visited:
                continue
            heapq.heappush(heap, (weight + nw, ne))

        shortest[edge] = weight

    return shortest


class DjikstraTest(unittest.TestCase):

    def test_djikstra(self):
        edges = [[0, 1, 2], [0, 2, 6], [2, 3, 8], [1, 3, 5], [3, 4, 10],
                 [3, 5, 15], [4, 5, 6], [4, 6, 2], [5, 6, 6]]
        shortest = [0, 2, 6, 7, 17, 22, 19]
        self.assertEqual(djikstra(edges), shortest)


if __name__ == "__main__":
    unittest.main()
