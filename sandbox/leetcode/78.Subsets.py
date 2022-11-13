import unittest


def subsets(nums):
    if not nums:
        return nums
    res = []

    def backtrack(subset, pos):
        if pos >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[pos])
        backtrack(subset, pos + 1)
        subset.pop()
        backtrack(subset, pos + 1)

    backtrack([], 0)
    return res


class SubsetsTest(unittest.TestCase):

    def test_subsets(self):
        self.assertCountEqual(subsets(
            [1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
        self.assertCountEqual(subsets([0]), [[], [0]])


if __name__ == "__main__":
    unittest.main()
