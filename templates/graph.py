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


def get_node_neighbors(grid, i, j):
    neighbors_positions = [
        [0, -1],  # left
        [0, 1],  # right
        [-1, 0],  # up
        [1, 0],  # down
    ]
    neighbors = []
    for pos in neighbors_positions:
        x = i + pos[0]
        y = j + pos[1]
        # checking row boundaries
        if not (0 <= x < len(grid)):
            continue
        # checking columns boundaries
        if not (0 <= y < len(grid[i])):
            continue
        neighbors.append(grid[x][y])
    return neighbors


class TestGraphNodeNeighbors(unittest.TestCase):

    def test_get_graph_node_neighbors(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(get_node_neighbors(grid, 1, 1), [4, 6, 2, 8])
        self.assertEqual(get_node_neighbors(grid, 0, 0), [2, 4])
        self.assertEqual(get_node_neighbors(grid, 2, 2), [8, 6])


if __name__ == "__main__":
    unittest.main()
