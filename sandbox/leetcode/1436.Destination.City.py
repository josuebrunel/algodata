import unittest


def destCity(paths):
    routes = {}
    for src, dst in paths:
        routes[src] = routes.get(src, 0) + 1
        routes[dst] = routes.get(dst, 0) - 1

    return min(routes, key=lambda x: routes[x])


class DestinationCityTest(unittest.TestCase):

    def test_destination_city(self):
        self.assertEqual(
            destCity([["London", "New York"], ["New York", "Lima"],
                      ["Lima", "Sao Paulo"]]), "Sao Paulo")
        self.assertEqual(destCity([["B", "C"], ["D", "B"], ["C", "A"]]), "A")
        self.assertEqual(destCity([["A", "Z"]]), "Z")


if __name__ == "__main__":
    unittest.main()
