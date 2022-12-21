import unittest
import collections


def majority_element(nums):
    counter = collections.Counter(nums)
    res = []
    for k, v in counter.items():
        if v > (len(nums) // 3):
            res.append(k)
    return res


class MajorityOfElementII(unittest.TestCase):

    def test_majority_element(self):
        self.assertEqual(majority_element([3, 2, 3]), [3])
        self.assertEqual(majority_element([1]), [1])
        self.assertEqual(majority_element([1, 2]), [1, 2])


if __name__ == "__main__":
    unittest.main()
