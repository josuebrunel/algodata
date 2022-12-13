import unittest


def cheapest_flights(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        tmp_prices = prices.copy()
        for s, d, p in flights:
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmp_prices[d]:
                tmp_prices[d] = tmp_prices[s] + p

        prices = tmp_prices

    return -1 if prices[dst] == float("inf") else prices[dst]


class CheapestFlightTest(unittest.TestCase):

    def test_cheapest_flight(self):
        self.assertEqual(
            cheapest_flights(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100],
                                 [1, 3, 600], [2, 3, 200]], 0, 3, 1), 700)
        self.assertEqual(
            cheapest_flights(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2,
                             1), 200)
        self.assertEqual(
            cheapest_flights(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2,
                             0), 500)


if __name__ == "__main__":
    unittest.main()
