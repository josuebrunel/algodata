import unittest
import collections
import heapq


def max_probability(n, edges, succProb, start, end):
    adj = collections.defaultdict(list)
    for (s, d), p in zip(edges, succProb):
        adj[s].append((d, p))
        adj[d].append((s, p))

    heap = []
    heapq.heappush(heap, (-1.0, start))
    distances = [0.0] * n
    distances[start] = -1.0
    seen = set()

    while heap:
        w, e = heapq.heappop(heap)

        if e in seen:
            continue
        if e == end:
            return -w
        seen.add(e)
        distances[e] = w
        for ne, nw in adj[e]:
            if nw in seen:
                continue
            heapq.heappush(heap, (nw * w, ne))

    return -distances[end]


class PathWithMaxProbability(unittest.TestCase):

    def test_path_with_max_probability(self):
        self.assertEqual(
            max_probability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0,
                            2), 0.25)
        self.assertEqual(
            max_probability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0,
                            2), 0.30)
        self.assertEqual(max_probability(3, [[0, 1]], [0.5], 0, 2), 0.0)


if __name__ == "__main__":
    unittest.main()
