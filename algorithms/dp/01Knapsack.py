import unittest


# O(2^N)
def max_profit(profit, weight, capacity):

    def dfs(i, profit, weight, cap):
        if i == len(profit):
            return 0

        # skip item
        maxProfit = dfs(i + 1, profit, weight, cap)
        # include item
        newCap = cap - weight[i]

        if newCap >= 0:
            p = profit[i] + dfs(i + 1, profit, weight, newCap)
            maxProfit = max(maxProfit, p)

        return maxProfit

    return dfs(0, profit, weight, capacity)


# O(N*M(Capacity))
def max_profit_with_cache(profit, weight, capacity):
    cache = {}

    def dfs(i, profit, weight, cap):

        if i == len(profit):
            return 0

        if cache.get((i, cap), None):
            return cache[(i, cap)]

        maxProfit = dfs(i + 1, profit, weight, cap)
        newCap = cap - weight[i]
        if newCap >= 0:
            p = profit[i] + dfs(i + 1, profit, weight, newCap)
            maxProfit = max(maxProfit, p)

        cache[(i, cap)] = maxProfit
        print(cache)
        return maxProfit

    return dfs(0, profit, weight, capacity)


# O(N*M) | O(N*M)
def max_profit_dp(profit, weight, capacity):
    # rows reprepsent the profit
    # cols represent the capacity
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # for each element in the first row
    # if the weitgh is less than the capacity
    # we update our dp table with the
    # corresponding profit
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = profit[0]

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i - 1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i - 1][c - weight[i]]
            dp[i][c] = max(skip, include)

    return dp[N - 1][M]


class ZeroOneKnapsackTest(unittest.TestCase):
    """
    Given a list of N items and a backpack with
    limited capacity, return the maximum total profit
    that can be obtained in the backpack. The i-th item
    profit is profit[i] and its weight is weight[i].
    Assume you can only add each item to the bag
    at most one time.
    """

    def test_max_profit(self):
        self.assertEqual(max_profit([4, 4, 7, 1], [5, 2, 3, 1], 8), 12)
        self.assertEqual(max_profit_with_cache([4, 4, 7, 1], [5, 2, 3, 1], 8),
                         12)
        self.assertEqual(max_profit_dp([4, 4, 7, 1], [5, 2, 3, 1], 8), 12)


if __name__ == "__main__":
    unittest.main()
