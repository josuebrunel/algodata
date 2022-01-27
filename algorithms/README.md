[kadane.py](#-kadanepy-)
[slidingwindow.py](#-slidingwindowpy-)
#### [ kadane.py ]( kadane.py )

```python

def kadane(array):
    msum = float("-inf")
    csum = float("-inf")
    for i in array:
        csum = max(i, csum + i)
        msum = max(msum, csum)
        print(csum, msum)
    return msum

if __name__ == "__main__":
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert kadane(array) == 6 # with [4, -1, 2, 1]

    # max(-2, 0-2) = -2, -2 
    # max(1, 1-2) = 1, 1
    # max(-3, -3+1 ) = -2, 1
    # max(4, 4-2) = 4, 4 
    # max(-1, -1+4) = 3, 4
    # max(2, 2+3 ) = 5, 5
    # max(1, 1+5) = 6, 6
    # max(-5, -5+6) = 1, 6
    # max(4, 4+1) = 5, 6


```



#### [ slidingwindow.py ]( slidingwindow.py )

```python

import unittest


def max_sum_subarray(array, k):
    if not array or k > len(array):
        return 0

    max_sum = 0

    for i in range(k):  # base line for k == len(array)
        max_sum += array[i]

    cur_sum = max_sum

    l, r = 0, k

    while r < len(array):
        cur_sum = cur_sum - array[l] + array[r]
        max_sum = max(max_sum, cur_sum)
        l += 1
        r += 1

    return max_sum


class MaxSumSubarray(unittest.TestCase):
    def test_max_sum_subarray(self):
        self.assertEqual(max_sum_subarray([], 3), 0)
        self.assertEqual(max_sum_subarray([1, 1, 1], 3), 3)
        self.assertEqual(max_sum_subarray([4, 2, 1, 6, 2], 4), 13)
        self.assertEqual(max_sum_subarray([4, 5, 7, 9, 20, 4, 9, 3, 11, 4, 3], 2), 29)
        self.assertEqual(max_sum_subarray([4, 5, 7, 9, 20, 4, 9, 3, 11, 4, 3], 3), 36)


if __name__ == "__main__":
    unittest.main()


```



