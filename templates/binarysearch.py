import unittest


def binarysearch(array, target):
    """A binary search algorithm is a simple decrease-and-conquer technique
    its goal is to find the position of a target value in a sorted array
    """
    left, right = 0, len(array)

    while left < right:
        # mid = (left + right) >> 1
        mid = left + (right - left) // 2
        mid_val = array[mid]
        if target == mid_val:
            return mid
        elif target > mid_val:
            left = mid + 1
        else:
            right = mid
    return -1


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binarysearch([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(binarysearch([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()
