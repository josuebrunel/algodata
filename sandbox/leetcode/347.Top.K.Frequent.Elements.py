import unittest
import heapq


# O(n) time | O(n) space
def top_k_frequent(nums, k):
    """The idea is to define a counter counting the
    number of occurences of an element, then mapping
    the occurences to the index of an array where each
    index represent a frequency.
    Once you have the array of frequency, you just have
    to iterate over it until you reach k
    """
    counter = {}
    freq = [[] for _ in range(len(nums) + 1)]
    # define a counter
    for n in nums:
        counter[n] = 1 + counter.get(n, 0)
    # set the frequency
    print(counter)
    # this is kind of bucket sort
    for n, c in counter.items():
        freq[c].append(n)

    print(freq)
    res = []
    i = len(freq) - 1
    while i >= 0:
        for c in freq[i]:
            res.append(c)
            k -= 1
            if k == 0:
                return res
        i -= 1

    return []


class TopKFrequentElementsTest(unittest.TestCase):
    def test_top_k_frequent(self):
        self.assertEqual(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(top_k_frequent([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
