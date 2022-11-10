import unittest


def kadaneMaxSubarray(array):
    maxSum = float("-inf")
    curSum = 0

    for n in array:
        curSum = max(n, n + curSum)
        maxSum = max(maxSum, curSum)

    return maxSum


def kadaneMaxSubarrayIJ(array):
    L = 0
    maxL, maxR = 0, 0
    curSum, maxSum = 0, float("-inf")

    for R in range(len(array)):
        if array[R] > curSum + array[R]:
            L = R
            curSum = array[R]
        else:
            curSum += array[R]

        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return array[maxL], array[maxR]


class KadaneTest(unittest.TestCase):

    def test_maximum_subarray(self):
        self.assertEqual(kadaneMaxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(kadaneMaxSubarray([1]), 1)
        self.assertEqual(kadaneMaxSubarray([5, 4, -1, 7, 8]), 23)

    def test_maximum_subarray_ij(self):
        self.assertEqual(kadaneMaxSubarrayIJ([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
                         (4, 1))
        self.assertEqual(kadaneMaxSubarrayIJ([1]), (1, 1))
        self.assertEqual(kadaneMaxSubarrayIJ([5, 4, -1, 7, 8]), (5, 8))


if __name__ == "__main__":
    unittest.main()
