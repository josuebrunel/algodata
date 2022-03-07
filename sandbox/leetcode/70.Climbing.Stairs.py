import unittest


def climb_stairs(n):
    if n in (1, 2):
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


class ClimbStairsTest(unittest.TestCase):
    def climb_stairs(self):
        self.assertEqual(climb_stairs(2), 2)
        self.assertEqual(climb_stairs(3), 3)
        self.assertEqual(climb_stairs(5), 8)
        self.assertEqual(climb_stairs(8), 34)


if __name__ == "__main__":
    unittest.main()
