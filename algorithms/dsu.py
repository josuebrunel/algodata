import unittest


class DSU:
    def __init__(self, array):
        self.array = array

    def __repr__(self):
        return f"{self.array}"

    def root(self, i):
        print(f"Looking for root {i}")
        while i != self.array[i]:
            # path compression
            self.array[i] = self.array[self.array[i]]
            i = self.array[i]
        print(f"Found root as {i}")
        return i

    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        self.array[root_a] = root_b

    def find(self, a, b):
        return self.root(a) == self.root(b)


class DSUTest(unittest.TestCase):
    def test_dsu(self):
        dsu = DSU([0, 1, 2, 3, 4, 5])
        dsu.union(0, 1)
        self.assertEqual((dsu.array[0], dsu.array[1]), (1, 1))
        self.assertEqual(dsu.find(1, 5), False)
        dsu.union(4, 5)
        self.assertEqual(dsu.find(4, 5), True)


if __name__ == "__main__":
    unittest.main()
