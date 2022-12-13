import collections
import unittest


class Graph:

    def __init__(self):
        self.graph = collections.defaultdict(list)

    def __repr__(self):
        return str(self.graph)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, vertex):
        q = collections.deque()
        seen = set()
        q.append(vertex)
        res = []

        while q:
            cur = q.popleft()
            seen.add(cur)
            for adj in self.graph[cur]:
                if adj in seen:
                    continue
                q.append(adj)
            res.append(cur)

        return res

    def shortest_path(self, start, end):
        q = collections.deque()
        q.append([start])
        seen = set()

        while q:
            path = q.popleft()
            v = path[-1]
            if v == end:
                return path

            if v in seen:
                continue

            seen.add(v)
            for n in self.graph[v]:
                new_path = list(path)
                new_path.append(n)
                q.append(new_path)

            path.append(v)

        return -1


class GraphBFS(unittest.TestCase):

    def test_graph_bfs(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        print(g)
        self.assertEqual(g.bfs(2), [2, 0, 3, 1])

    def test_shortest_path(self):
        g = Graph()
        g.graph = {
            'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']
        }
        self.assertEqual(g.shortest_path("A", "D"), ["A", "B", "D"])


if __name__ == "__main__":
    unittest.main()
