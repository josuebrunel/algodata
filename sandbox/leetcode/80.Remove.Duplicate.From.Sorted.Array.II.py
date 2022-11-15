import unittest


def remove_duplicate(nums):
    L = 2
    for R in range(2, len(nums)):
        if nums[R] != nums[L - 2]:
            nums[L] = nums[R]
            L += 1

    return L


class RemoveDuplicateInSortedArrayTest(unittest.TestCase):

    def test_remove_duplicate(self):
        self.assertEqual(remove_duplicate([1, 1, 1, 2, 2, 3]), 5)
        self.assertEqual(remove_duplicate([0, 0, 1, 1, 1, 1, 2, 3, 3]), 7)


if __name__ == "__main__":
    unittest.main()
