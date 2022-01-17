import unittest


# O(amount * len(coins)) time | O(amount) space
def coin_change(coins, amount):
    """The idea is to generate all the possible ways
    for each coin to make change for the amount then
    taking the minimum amount for the current amount
    (current amount going from 0 to amount) between
    the existing number of change and the new computed
    number of change.
    """

    # we populate an array of changes
    changes = [amount + 1] * (amount + 1)
    # we need 0 coin to make a change of 0
    changes[0] = 0
    # for each amount from 1 to amount + 1
    for i in range(1, amount + 1):
        # for each coin
        for c in coins:
            # if the current coin is less or equal
            # to the current amount
            if c <= i:
                # we take the minimum number of changes between
                # current minimum number of changes for the current
                # amount and one (1) plus the current amount minus
                # the current coin
                changes[i] = min(changes[i], 1 + changes[i - c])
        print(changes)
    return changes[amount] if changes[amount] != amount + 1 else -1


class CoinChangeTest(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(coin_change([2], 3), -1)
        self.assertEqual(coin_change([1], 0), 0)
        self.assertEqual(coin_change([2, 4, 5], 9), 2)


if __name__ == "__main__":
    unittest.main()
