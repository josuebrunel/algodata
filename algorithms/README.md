* [binarysearch.py](#-binarysearchpy-)
* [kadane.py](#-kadanepy-)
* [monotonicstack.py](#-monotonicstackpy-)
* [slidingwindow.py](#-slidingwindowpy-)
#### [ binarysearch.py ]( binarysearch.py )

```python

import unittest


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid
    return -1


def binary_search_matrix(matrix, target):
    row, col = 0, len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if target > matrix[row][col]:
            row += 1
        elif target < matrix[row][col]:
            col -= 1
        else:
            return True

    return False


class BinaraySearchTest(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(binary_search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_binary_search_matrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertIs(binary_search_matrix(matrix, 3), True)
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertIs(binary_search_matrix(matrix, 13), False)


if __name__ == "__main__":
    unittest.main()


```



#### [ kadane.py ]( kadane.py )

```python

import unittest


def kadaneMaxSubarray(array):
    maxSum = float("-inf")
    curSum = 0

    for n in array:
        curSum = max(n, n + curSum)
        maxSum = max(maxSum, curSum)

    return maxSum


def kadaneMaxSubarrayIJ(array):
    L = 0
    maxL, maxR = 0, 0
    curSum, maxSum = 0, float("-inf")

    for R in range(len(array)):
        if array[R] > curSum + array[R]:
            L = R
            curSum = array[R]
        else:
            curSum += array[R]

        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return array[maxL], array[maxR]


class KadaneTest(unittest.TestCase):

    def test_maximum_subarray(self):
        self.assertEqual(kadaneMaxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(kadaneMaxSubarray([1]), 1)
        self.assertEqual(kadaneMaxSubarray([5, 4, -1, 7, 8]), 23)

    def test_maximum_subarray_ij(self):
        self.assertEqual(kadaneMaxSubarrayIJ([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
                         (4, 1))
        self.assertEqual(kadaneMaxSubarrayIJ([1]), (1, 1))
        self.assertEqual(kadaneMaxSubarrayIJ([5, 4, -1, 7, 8]), (5, 8))


if __name__ == "__main__":
    unittest.main()


```



#### [ monotonicstack.py ]( monotonicstack.py )

```python

import unittest


def increasing_mono_stack(nums):
    stack = []

    for i in range(len(nums)):
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        stack.append(nums[i])
    return stack


def decreasing_mono_stack(nums):
    stack = []
    for i in range(len(nums)):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        stack.append(nums[i])
    return stack


class MonoStackTest(unittest.TestCase):

    def test_increasing_mono_stack(self):
        self.assertEqual(increasing_mono_stack([5, 3, 1, 2, 4]), [1, 2, 4])

    def test_decreasing_mono_stack(self):
        self.assertEqual(decreasing_mono_stack([5, 3, 1, 2, 4]), [5, 4])


if __name__ == "__main__":
    unittest.main()


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



