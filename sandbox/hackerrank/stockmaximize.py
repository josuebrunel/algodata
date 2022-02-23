import unittest


def stockmax(prices):
    profit, curMax = 0, 0

    for i in range(len(prices) - 1, -1, -1):
        curMax = max(curMax, prices[i])
        profit += curMax - prices[i]

    return profit


class MaximizeStockTest(unittest.TestCase):
    def test_stock_maximize(self):
        prices = [5, 3, 2]
        self.assertEqual(stockmax(prices), 0)
        prices = [1, 2, 100]
        self.assertEqual(stockmax(prices), 197)
        prices = [1, 3, 1, 2]
        self.assertEqual(stockmax(prices), 3)


if __name__ == "__main__":
    unittest.main()
