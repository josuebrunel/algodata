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
