import unittest
import heapq


def last_stone_weight(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        if first < second:
            heapq.heappush(stones, first - second)

    return -stones[0] if stones else 0


class LastStoneWeightTest(unittest.TestCase):

    def test_last_stone_weight(self):
        self.assertEqual(last_stone_weight([2, 7, 4, 1, 8, 1]), 1)


if __name__ == "__main__":
    unittest.main()
