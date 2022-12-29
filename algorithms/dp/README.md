* [01Knapsack.py](#-01Knapsackpy-)
* [fibonacci.py](#-fibonaccipy-)
* [lcs.py](#-lcspy-)
#### [ 01Knapsack.py ]( 01Knapsack.py )

```python

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


```



#### [ fibonacci.py ]( fibonacci.py )

```python

import unittest


def fibonacci_recursive(n):
    if n <= 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dp(n):
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fibonacci(n):
    if n < 2:
        return 1

    prev, cur = 1, 1
    for i in range(3, n + 1):
        csum = prev + cur
        prev = cur
        cur = csum

    return cur


class FibonacciTest(unittest.TestCase):
    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(10), 55)

    def test_fibonacci_dp(self):
        pass
        self.assertEqual(fibonacci_dp(10), 55)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), 55)


if __name__ == "__main__":
    unittest.main()


```



#### [ lcs.py ]( lcs.py )

```python

import unittest


# O(2^(N+M)) | O(N+M)
def lcs_dfs(s1, s2):

    def dfs(s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return 0

        if s1[i] == s2[j]:
            return 1 + dfs(s1, s2, i + 1, j + 1)

        return max(dfs(s1, s2, i + 1, j), dfs(s1, s2, i, j + 1))

    return dfs(s1, s2, 0, 0)


# O(N*M) | O(N+M)
def lcs_with_cache(s1, s2):

    cache = {}

    def dfs(s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        if s1[i] == s2[j]:
            cache[(i, j)] = 1 + dfs(s1, s2, i + 1, j + 1)
            return cache[(i, j)]

        cache[(i, j)] = max(dfs(s1, s2, i + 1, j), dfs(s1, s2, i, j + 1))
        return cache[(i, j)]

    return dfs(s1, s2, 0, 0)


# O(N*M) | O(N+M)
def lcs_dp(s1, s2):
    N, M = len(s1), len(s2)
    dp = {(i, j): 0 for i in range(N + 1) for j in range(M + 1)}

    for i in range(N):
        for j in range(M):
            if s1[i] == s2[j]:
                dp[(i + 1, j + 1)] = 1 + dp[(i, j)]
            else:
                dp[(i + 1, j + 1)] = max(dp[(i + 1, j)], dp[(i, j + 1)])

    return dp[(N, M)]


class LCSTest(unittest.TestCase):
    """
    Given two strings S1 and S2, find
    the length of the longest common
    subsequence between the two strings
    """

    def test_lcs_dfs(self):
        self.assertEqual(lcs_dfs("adcb", "abc"), 2)
        self.assertEqual(lcs_dfs("abcde", "ace"), 3)
        self.assertEqual(lcs_dfs("abc", "def"), 0)
        self.assertEqual(lcs_dfs("", "abc"), 0)

    def test_lcs_with_cache(self):
        self.assertEqual(lcs_with_cache("adcb", "abc"), 2)
        self.assertEqual(lcs_with_cache("abcde", "ace"), 3)
        self.assertEqual(lcs_with_cache("abc", "def"), 0)
        self.assertEqual(lcs_with_cache("", "abc"), 0)

    def test_lcs_dp(self):
        self.assertEqual(lcs_dp("adcb", "abc"), 2)
        self.assertEqual(lcs_dp("abcde", "ace"), 3)
        self.assertEqual(lcs_dp("abc", "def"), 0)
        self.assertEqual(lcs_dp("", "abc"), 0)


if __name__ == "__main__":
    unittest.main()


```



