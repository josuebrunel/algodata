import unittest


def max_sum_subarray(array, k):
    if not array or k > len(array):
        return 0

    max_sum = 0

    for i in range(k):  # base line for k == len(array)
        max_sum += array[i]

    cur_sum = max_sum

    l, r = 0, k

    while r < len(array):
        cur_sum = cur_sum - array[l] + array[r]
        max_sum = max(max_sum, cur_sum)
        l += 1
        r += 1

    return max_sum


class MaxSumSubarray(unittest.TestCase):
    def test_max_sum_subarray(self):
        self.assertEqual(max_sum_subarray([], 3), 0)
        self.assertEqual(max_sum_subarray([1, 1, 1], 3), 3)
        self.assertEqual(max_sum_subarray([4, 2, 1, 6, 2], 4), 13)
        self.assertEqual(max_sum_subarray([4, 5, 7, 9, 20, 4, 9, 3, 11, 4, 3], 2), 29)
        self.assertEqual(max_sum_subarray([4, 5, 7, 9, 20, 4, 9, 3, 11, 4, 3], 3), 36)


if __name__ == "__main__":
    unittest.main()
