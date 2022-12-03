import unittest


def overlap(a, b):
    """To check if 2 intervals (A and B) overlap we naturally
    check that the if Aj > Bi or Bj > Ai. Another is to check
    if min(Aj, Bj) - max(Ai, Bi) >= 0
    """
    front = max(a[0], b[0])
    back = min(a[1], b[1])
    return back - front >= 0


class IntervalsOverlapTest(unittest.TestCase):
    def test_overlap(self):
        self.assertEqual(overlap([1, 4], [3, 5]), True)
        self.assertEqual(overlap([1, 2], [0, 4]), True)
        self.assertEqual(overlap([0, 2], [4, 5]), False)


if __name__ == "__main__":
    unittest.main()
