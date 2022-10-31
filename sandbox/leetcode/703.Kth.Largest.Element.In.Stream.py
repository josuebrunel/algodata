import unittest
import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


class KthLargestElementTest(unittest.TestCase):

    def test_kth_largest_element(self):
        obj = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(obj.add(3), 4)
        self.assertEqual(obj.add(5), 5)
        self.assertEqual(obj.add(10), 5)
        self.assertEqual(obj.add(9), 8)
        self.assertEqual(obj.add(4), 8)


if __name__ == "__main__":
    unittest.main()
