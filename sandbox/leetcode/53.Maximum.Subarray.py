import unittest


def maxSubarray(nums):
    maxSum = float("-inf")
    curSum = 0

    for n in nums:
        curSum = max(n, n + curSum)
        maxSum = max(maxSum, curSum)

    return maxSum


class MaximumSubarrayTest(unittest.TestCase):

    def test_maximum_subarray(self):
        self.assertEqual(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maxSubarray([1]), 1)
        self.assertEqual(maxSubarray([5, 4, -1, 7, 8]), 23)


if __name__ == "__main__":
    unittest.main()
