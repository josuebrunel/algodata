* [heap.py](#-heappy-)
#### [ heap.py ]( heap.py )

```python

import unittest


# O(log(n) time
# O(n) space : we don't need more than the array holding the values
class MaxHeap:
    def __init__(self):
        self.array = []

    def __repr__(self):
        return f"{self.array}"

    def peek(self):
        if not self.array:
            return None
        return self.array[0]

    # O(log(n) time because of the logarithmic relationship between an index and its children
    def insert(self, val):
        """Adds an element to the heap"""
        self.array.append(val)
        self._heapify_up(len(self.array) - 1)

    def _heapify_up(self, index):
        """Heapifies the heap from bottom top"""
        while self.array[self.parent_idx(index)] < self.array[index]:
            parent = self.parent_idx(index)
            self.array[parent], self.array[index] = (
                self.array[index],
                self.array[parent],
            )
            index = parent

    # O(log(n) time because of the logarithmic relationship between an index and its children
    def extract(self):
        """Removes an element from the heap"""
        if not self.array:
            return None
        root = self.array[0]
        self.array[0] = self.array[-1]
        self.array = self.array[: len(self.array) - 1]
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        """Heapifies the heap top bottom"""
        last_index = len(self.array) - 1
        left, right = self.left_child_idx(index), self.right_child_idx(index)
        child_to_compare = 0
        # loop while index has at least one child
        while left <= last_index:
            # if left child the only child
            if left == last_index:
                child_to_compare = left
            # if left child is larger
            elif self.array[left] > self.array[right]:
                child_to_compare = left
            # if right is larger
            else:
                child_to_compare = right

            # compare value of current index to child to compare
            # then swap if child is larger
            if self.array[index] < self.array[child_to_compare]:
                self.array[index], self.array[child_to_compare] = (
                    self.array[child_to_compare],
                    self.array[index],
                )
                index = child_to_compare
                left, right = self.left_child_idx(index), self.right_child_idx(index)
            else:
                return

    @staticmethod
    def parent_idx(index):
        """Returns the parent's index of a given index"""
        parent = (index - 1) // 2
        if parent < 0:
            return 0
        return parent

    @staticmethod
    def left_child_idx(index):
        """Returns the left child of a given index"""
        return (index * 2) + 1

    @staticmethod
    def right_child_idx(index):
        """Returns the right child of a given index"""
        return (index * 2) + 2


class TestHeap(unittest.TestCase):
    def test_max_heap(self):
        h = MaxHeap()
        for i in [10, 20, 30]:
            h.insert(i)
        print(h)
        self.assertEqual(h.array, [30, 10, 20])
        for i in [5, 15, 25, 35]:
            h.insert(i)
        print(h)
        for _ in range(4):
            h.extract()
            print(h)
        self.assertEqual(h.array, [15, 5, 10])


if __name__ == "__main__":
    unittest.main()


```



