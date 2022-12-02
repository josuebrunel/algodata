import unittest


def daily_temperatues(temps):
    ans = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and stack[-1][0] < t:
            val, idx = stack.pop()
            ans[idx] = i - idx
        stack.append((t, i))
    return ans


class DailyTemperatuesTest(unittest.TestCase):

    def test_daily_temperatures(self):
        self.assertEqual(daily_temperatues([73, 74, 75, 71, 69, 72, 76, 73]),
                         [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(daily_temperatues([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(daily_temperatues([30, 60, 90]), [1, 1, 0])


if __name__ == "__main__":
    unittest.main()
