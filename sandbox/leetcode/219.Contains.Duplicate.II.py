import unittest


def containsDuplicate(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


class ContainsDuplicateII(unittest.TestCase):

    def test_contains_duplicate_ii(self):
        self.assertEqual(containsDuplicate([1, 2, 3, 1], 3), True)
        self.assertEqual(containsDuplicate([1, 0, 1, 1], 1), True)
        self.assertEqual(containsDuplicate([1, 2, 3, 1, 2, 3], 2), False)


if __name__ == "__main__":
    unittest.main()
