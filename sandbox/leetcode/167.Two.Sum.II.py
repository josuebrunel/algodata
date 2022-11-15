import unittest


def two_sum(nums, target):
    L, R = 0, len(nums) - 1

    while L < R:
        curSum = nums[L] + nums[R]
        if curSum > target:
            R -= 1
        elif curSum < target:
            L += 1
        else:
            break

    return [L + 1, R + 1]


class TwoSumIITest(unittest.TestCase):

    def test_2_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(two_sum([2, 3, 4], 6), [1, 3])
        self.assertEqual(two_sum([-1, 0], -1), [1, 2])


if __name__ == "__main__":
    unittest.main()
