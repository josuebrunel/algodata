* [binarysearch.py](#-binarysearchpy-)
* [graph.py](#-graphpy-)
* [intervals.py](#-intervalspy-)
* [linkedlist.py](#-linkedlistpy-)
* [monotonicstack.py](#-monotonicstackpy-)
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



#### [ graph.py ]( graph.py )

```python

import collections
import unittest


class Graph:

    def __init__(self):
        self.graph = collections.defaultdict(list)

    def __repr__(self):
        return str(self.graph)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, vertex):
        q = collections.deque()
        seen = set()
        q.append(vertex)
        res = []

        while q:
            cur = q.popleft()
            seen.add(cur)
            for adj in self.graph[cur]:
                if adj in seen:
                    continue
                q.append(adj)
            res.append(cur)

        return res


class GraphBFS(unittest.TestCase):

    def test_graph_bfs(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        print(g)
        self.assertEqual(g.bfs(2), [2, 0, 3, 1])


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



#### [ intervals.py ]( intervals.py )

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



#### [ linkedlist.py ]( linkedlist.py )

```python

def reverse(head):
    prev, cur = None, head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    head = prev
    return head


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



