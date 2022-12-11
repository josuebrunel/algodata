import unittest
import collections
import heapq


def network_delay(times, n, k):
    adj = collections.defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
        adj[v] = adj[v]

    seen = set()
    heap = []
    heapq.heappush(heap, (0, k))
    res = []
    while heap:
        w, e = heapq.heappop(heap)
        if e in seen:
            continue
        seen.add(e)
        res.append(w)
        for ne, nw in adj[e]:
            if ne in seen:
                continue
            heapq.heappush(heap, (w + nw, ne))

    # print(res, n)
    return -1 if len(res) < n else res[n - 1]


class NetworkDelay(unittest.TestCase):

    def test_network_delay(self):
        self.assertEqual(
            network_delay([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)
        self.assertEqual(network_delay([[1, 2, 1]], 2, 1), 1)
        self.assertEqual(network_delay([[1, 2, 1]], 2, 2), -1)


if __name__ == "__main__":
    unittest.main()
