import unittest
import heapq


def kClosest(points, k):
    points = [((pt[0] - 0)**2 + (pt[1] - 0)**2, pt) for pt in points]
    heapq.heapify(points)
    res = []
    while k > 0:
        _, pt = heapq.heappop(points)
        res.append(pt)
        k -= 1
    return res


class KClosestToOriginTest(unittest.TestCase):

    def test_k_closest_to_origin(self):
        self.assertEqual(kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertCountEqual(kClosest([[3, 3], [5, -1], [-2, 4]], 2),
                              [[-2, 4], [3, 3]])


if __name__ == "__main__":
    unittest.main()
