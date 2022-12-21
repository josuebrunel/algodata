import unittest


def sum_of_three(num):
    half = num // 3
    prv, nxt = half - 1, half + 1

    if prv + half + nxt == num:
        return [prv, half, nxt]
    return []


class Find3ConsecutiveIntThatSumToK(unittest.TestCase):

    def test_sum_of_three(self):
        self.assertEqual(sum_of_three(33), [10, 11, 12])
        self.assertEqual(sum_of_three(4), [])


if __name__ == "__main__":
    unittest.main()
