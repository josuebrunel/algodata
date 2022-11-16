import unittest


def max_area(height):
    L, R = 0, len(height) - 1
    res = 0

    while L < R:
        curMin = min(height[L], height[R])
        res = max(res, curMin * (R - L))
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1

    return res


class ContainerWithMostWaterTest(unittest.TestCase):

    def test_max_area(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(max_area([1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
