import unittest


class NumArray:

    def __init__(self, nums):
        self.prefix = []
        for n in nums:
            self.prefix.append(n + self.prefix[-1] if self.prefix else n)

    def sumRange(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return preRight - preLeft


class NumArrayTest(unittest.TestCase):

    def test_num_array(self):
        na = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(na.sumRange(0, 2), 1)
        self.assertEqual(na.sumRange(2, 5), -1)
        self.assertEqual(na.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
