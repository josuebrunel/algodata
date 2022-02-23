import unittest


def max_profit(prices):
    left, right = 0, 1
    maxProfit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            print(prices, prices[left], prices[right])
            maxProfit = max(maxProfit, prices[right] - prices[left])
        else:
            left = right
        right += 1
    return maxProfit


class MaxProfitTest(unittest.TestCase):
    def test_max_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)


if __name__ == "__main__":
    unittest.main()
