[binarysearch.py](#-binarysearchpy-)
[graph_neighbors.py](#-graph_neighborspy-)
[intervals_overlap.py](#-intervals_overlappy-)
[monotonicstack.py](#-monotonicstackpy-)
#### [ binarysearch.py ]( binarysearch.py )

```python

import unittest


def binarysearch(array, target):
    """A binary search algorithm is a simple decrease-and-conquer technique
    its goal is to find the position of a target value in a sorted array
    """
    left, right = 0, len(array)

    while left < right:
        # mid = (left + right) >> 1
        mid = left + (right - left) // 2
        mid_val = array[mid]
        if target == mid_val:
            return mid
        elif target > mid_val:
            left = mid + 1
        else:
            right = mid
    return -1


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binarysearch([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(binarysearch([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()


```



#### [ graph_neighbors.py ]( graph_neighbors.py )

```python

import unittest


def get_node_neighbors(grid, i, j):
    neighbors_positions = [
        [0, -1],  # left
        [0, 1],  # right
        [-1, 0],  # up
        [1, 0],  # down
    ]
    neighbors = []
    for pos in neighbors_positions:
        x = i + pos[0]
        y = j + pos[1]
        # checking row boundaries
        if not (0 <= x < len(grid)):
            continue
        # checking columns boundaries
        if not (0 <= y < len(grid[i])):
            continue
        neighbors.append(grid[x][y])
    return neighbors


class TestGraphNodeNeighbors(unittest.TestCase):
    def test_get_graph_node_neighbors(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(get_node_neighbors(grid, 1, 1), [4, 6, 2, 8])
        self.assertEqual(get_node_neighbors(grid, 0, 0), [2, 4])
        self.assertEqual(get_node_neighbors(grid, 2, 2), [8, 6])


if __name__ == "__main__":
    unittest.main()


```



#### [ intervals_overlap.py ]( intervals_overlap.py )

```python

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



