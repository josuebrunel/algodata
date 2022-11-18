import unittest


def find_pivot_index(nums):
    prefix = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = prefix - nums[i] - leftSum
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1


class FindPivotIndexClass(unittest.TestCase):

    def test_find_pivot_index(self):
        self.assertEqual(find_pivot_index([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(find_pivot_index([1, 2, 3]), -1)
        self.assertEqual(find_pivot_index([2, 1, -1]), 0)


if __name__ == "__main__":
    unittest.main()
