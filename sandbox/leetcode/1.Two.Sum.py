import unittest


def two_sum(nums, target):
    prefix = {}
    for i in range(len(nums)):
        sub = target - nums[i]
        if sub in prefix:
            return [prefix[sub], i]
        prefix[nums[i]] = i


class TwoSumTest(unittest.TestCase):

    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
