import unittest
import heapq


def find_kth_largest(nums, k):
    maxheap = []
    for i in nums[:k]:
        heapq.heappush(maxheap, i)

    print(maxheap)
    for i in nums[k:]:
        if i > maxheap[0]:
            heapq.heappop(maxheap)
            heapq.heappush(maxheap, i)
    print(maxheap)
    return maxheap[0]


class FindKthLargestTest(unittest.TestCase):
    def test_find_kth_largest(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
        self.assertEqual(find_kth_largest([2, 1], 1), 2)


if __name__ == "__main__":
    unittest.main()
