import unittest


def longest_consecutive_sequence(nums):
    """The idea is to put every number in nums
    in a set and check if num - 1 exists in that set.
    If num - 1 exists, it means that we have a sequence.
    Then as long as num + length (where length represents
    the length of the current sequence)  exists in the set
    we increase the length of the set
    """
    numSet = set(nums)
    longest = 0

    for i in nums:
        # check if start of a sequence
        if i - 1 not in numSet:
            length = 0
            # as long as it's a sequence
            # increase its length
            while i + length in numSet:
                length += 1
            longest = max(longest, length)
    return longest


class LongestConsecutiveSequenceTest(unittest.TestCase):
    def test_longest_consecutive_sequence(self):
        self.assertEqual(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(
            longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9
        )


if __name__ == "__main__":
    unittest.main()
