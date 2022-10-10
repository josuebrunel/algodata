import unittest


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return a


class FibonacciNumberTest(unittest.TestCase):

    def test_fibonacci_number(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(10), 55)


if __name__ == "__main__":
    unittest.main()
