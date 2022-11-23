import unittest


def combine(n, k):
    res = []

    def backtrack(i, comb):
        if len(comb) == k:
            res.append(comb.copy())
            return

        for j in range(i, n + 1):
            comb.append(j)
            backtrack(j + 1, comb)
            comb.pop()

    backtrack(1, [])
    return res


class CombinationsTest(unittest.TestCase):

    def test_combination(self):
        self.assertCountEqual(combine(4, 2),
                              [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
        self.assertCountEqual(combine(1, 1), [[1]])


if __name__ == "__main__":
    unittest.main()
