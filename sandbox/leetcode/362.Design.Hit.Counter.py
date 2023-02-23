import unittest
import collections


class HitCounter:

    def __init__(self):
        self.counter = collections.Counter()

    def hit(self, ts):
        self.counter[ts] += 1

    def getHits(self, ts):
        res = 0
        for t, c in self.counter.items():
            if t + 300 > ts:
                res += c

        return res


class HitCounterTest(unittest.TestCase):

    def test_hit_counter(self):
        hc = HitCounter()
        for i in range(1, 4):
            hc.hit(i)

        self.assertEqual(hc.getHits(4), 3)
        hc.hit(300)
        print(hc.counter)
        self.assertEqual(hc.getHits(300), 4)
        self.assertEqual(hc.getHits(301), 3)


if __name__ == "__main__":
    unittest.main()
