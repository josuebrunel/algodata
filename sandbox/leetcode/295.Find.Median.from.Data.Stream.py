import unittest
import heapq


class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []

    def addNumber(self, num):
        heapq.heappush(self.min, -num)
        if self.min and self.max and -self.min[0] > self.max[0]:
            val = heapq.heappop(self.min)
            heapq.heappush(self.max, -val)

        if len(self.min) > len(self.max) + 1:
            val = heapq.heappop(self.min)
            heapq.heappush(self.max, -val)
        if len(self.max) > len(self.min) + 1:
            val = heapq.heappop(self.max)
            heapq.heappush(self.min, -val)

    def findMedian(self):
        if len(self.min) > len(self.max):
            return -self.min[0]
        elif len(self.min) < len(self.max):
            return self.max[0]
        else:
            return (-self.min[0] + self.max[0]) / 2


class MedianFinderTest(unittest.TestCase):

    def test_median_class(self):
        m = MedianFinder()
        m.addNumber(1)
        m.addNumber(2)
        self.assertEqual(m.findMedian(), 1.5)
        m.addNumber(3)
        self.assertEqual(m.findMedian(), 2)

        m = MedianFinder()
        m.addNumber(-1)
        self.assertEqual(m.findMedian(), -1)
        m.addNumber(-2)
        self.assertEqual(m.findMedian(), -1.5)
        m.addNumber(-3)
        self.assertEqual(m.findMedian(), -2)
        m.addNumber(-4)
        self.assertEqual(m.findMedian(), -2.5)
        m.addNumber(-5)
        self.assertEqual(m.findMedian(), -3)


if __name__ == "__main__":
    unittest.main()
