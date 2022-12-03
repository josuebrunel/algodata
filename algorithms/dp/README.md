* [fibonacci.py](#-fibonaccipy-)
#### [ fibonacci.py ]( fibonacci.py )

```python

import unittest


def fibonacci_recursive(n):
    if n <= 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dp(n):
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fibonacci(n):
    if n < 2:
        return 1

    prev, cur = 1, 1
    for i in range(3, n + 1):
        csum = prev + cur
        prev = cur
        cur = csum

    return cur


class FibonacciTest(unittest.TestCase):
    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(10), 55)

    def test_fibonacci_dp(self):
        pass
        self.assertEqual(fibonacci_dp(10), 55)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), 55)


if __name__ == "__main__":
    unittest.main()


```



