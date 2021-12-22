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
        if not (0 <= x < len(grid[i])):
            continue
        # checking columns boundaries
        if not (0 <= y < len(grid)):
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



