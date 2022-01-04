import unittest
import logging


logger = logging.getLogger(__name__)


class Vertex:
    def __init__(self, key):
        self.key = key
        self.adjacent = []

    def __repr__(self):
        return f"{self.key} : {self.adjacent}\n"


class Graph:
    def __init__(self):
        self.vertices = []

    def __repr__(self):
        return f"{self.vertices}"

    def add_vertex(self, key):
        """Adds a vertex to the graph"""
        if self.contains(key):
            return
        vertex = Vertex(key)
        self.vertices.append(vertex)

    def contains(self, key):
        """Checks if a vertex exists in the graph"""
        for vertex in self.vertices:
            if vertex.key == key:
                return True
        return False

    def get_vertex(self, key):
        """Returns a vertex if exists in the graph"""
        for vertex in self.vertices:
            if vertex.key == key:
                return vertex
        return

    def add_edge(self, src, dst):
        """Adds edge between 2 vertices"""
        src_vertex = self.get_vertex(src)
        dst_vertex = self.get_vertex(dst)
        # if source or destination doesn't exist, throw execption
        if not src_vertex or not dst_vertex:
            logger.error("source or destination vertex doesn't exist")
            return
        # prevent edge duplication
        for v in src_vertex.adjacent:
            if v.key == dst_vertex.key:
                logger.error("An edge already exists between those 2 vertices")
                return
        src_vertex.adjacent.append(dst_vertex)


class TestGraph(unittest.TestCase):
    def test_graph(self):
        graph = Graph()
        for i in range(5):
            graph.add_vertex(i)
        print(graph)
        self.assertEqual(len(graph.vertices), 5)
        graph.add_edge(1, 2)
        graph.add_edge(1, 2)
        graph.add_edge(3, 2)
        graph.add_edge(4, 6)
        print(graph)


if __name__ == "__main__":
    unittest.main()
