* [binarysearch.py](#-binarysearchpy-)
* [graph.py](#-graphpy-)
* [intervals.py](#-intervalspy-)
* [linkedlist.py](#-linkedlistpy-)
* [monotonicstack.py](#-monotonicstackpy-)
* [tree.py](#-treepy-)
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

    def shortest_path(self, start, end):
        q = collections.deque()
        q.append([start])
        seen = set()

        while q:
            path = q.popleft()
            v = path[-1]
            if v == end:
                return path

            if v in seen:
                continue

            seen.add(v)
            for n in self.graph[v]:
                new_path = list(path)
                new_path.append(n)
                q.append(new_path)

            path.append(v)

        return -1


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

    def test_shortest_path(self):
        g = Graph()
        g.graph = {
            'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']
        }
        self.assertEqual(g.shortest_path("A", "D"), ["A", "B", "D"])


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



#### [ tree.py ]( tree.py )

```python

def invert_binary_tree(root):
    """Swap left and right children
    """
    if not root:
        return
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(
        root.left)
    return root


def max_depth_binary_tree(root):
    """Take the max value between
    the depth of the left child and right child
    """
    if not root:
        return 0
    return 1 + max(max_depth_binary_tree(root.left),
                   max_depth_binary_tree(root.right))


def diameter_binary_tree(root):
    """Take the max diameter between
    the left and right child and add 1 to it.
    """
    res = [0]

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        res[0] = max(res[0], left, right)
        return 1 + max(left, right)

    dfs(root)

    return res


def balance_binary_tree(root):
    """A binary tree is balanced if the diff of depth
    between the left and right child is not > 1
    """
    if not root:
        return True

    def dfs(node):
        if not node:
            return [True, 0]

        left = dfs(node.left)
        right = dfs(node.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return balanced, 1 + max(left, right)

    return dfs(root)[0]


def same_binary_tree(p, q):
    """2 Binary tree are the same if every nodes
    has the same value at the same position for
    both trees
    """
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return same_binary_tree(p.left, q.left) and same_binary_tree(
            p.right, q.right)
    return False


```



