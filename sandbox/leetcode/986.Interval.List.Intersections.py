import unittest


def interval_intersection(l1, l2):
    res = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        start = max(l1[i][0], l2[j][0])
        end = min(l1[i][1], l2[j][1])
        print(l1[i], l2[j], start, end)
        if start <= end:
            res.append([start, end])
        if l1[i][1] == end:
            i += 1
        else:
            j += 1
    return res


class IntervalListIntersections(unittest.TestCase):
    def test_interval_intersection(self):
        self.assertEqual(
            interval_intersection(
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [[1, 5], [8, 12], [15, 24], [25, 26]],
            ),
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        )
        self.assertEqual(interval_intersection([[1, 3], [5, 9]], []), [])


if __name__ == "__main__":
    unittest.main()
