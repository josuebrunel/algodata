import unittest


def minSubarrayLen(array, target):
    L, curSum = 0, 0
    res = float("inf")
    for R in range(len(array)):
        curSum += array[R]
        while curSum >= target:
            res = min(res, len(array[L:R + 1]))
            curSum -= array[L]
            L += 1

    return 0 if res == float("inf") else res


class MinimumSizeSubarraySumTest(unittest.TestCase):

    def test_min_subarray_len(self):
        self.assertEqual(minSubarrayLen([2, 3, 1, 2, 4, 3], 7), 2)
        self.assertEqual(minSubarrayLen([1, 4, 4], 4), 1)
        self.assertEqual(minSubarrayLen([1, 1, 1, 1, 1, 1, 1, 1], 11), 0)


if __name__ == "__main__":
    unittest.main()
