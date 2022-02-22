import unittest


def is_power_of_two(n):
    if n < 1:
        return False

    while n >= 2:
        if n % 2 == 0:
            n /= n
        else:
            return False
    return True


class PowerOfTwoTest(unittest.TestCase):
    def test_power_of_two(self):
        self.assertEqual(is_power_of_two(1), True)
        self.assertEqual(is_power_of_two(16), True)
        self.assertEqual(is_power_of_two(3), False)


if __name__ == "__main__":
    unittest.main()
