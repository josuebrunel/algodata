[bubble.py](#-bubblepy-)
[cyclic.py](#-cyclicpy-)
[insertion.py](#-insertionpy-)
[selection.py](#-selectionpy-)
#### [ bubble.py ]( bubble.py )

```python

import unittest


# O(n^2) time | O(1)
def bubble_sort(array):
    """The idea is to compare the i(th) to the i+1(th) element
    and swap them is i > i+1.
    At the end of the first iteration, the biggest element of the array
    will be at the end of this array. Thus for the rest of the iterations
    we sort from 0 to len(array) - i - counter with counter equal to the number
    of elements already properly sorted
    """
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        counter += 1
    return array


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        array = [8, 5, 2, 9, 5, 6, 3]
        self.assertEqual(bubble_sort(array), sorted(array))


if __name__ == "__main__":
    unittest.main()


```



#### [ cyclic.py ]( cyclic.py )

```python

import unittest


# O(n) time | O(1) space
def cyclic_sort(array):
    """The idea is to put every value at its right postion
    according the relation index = value - 1.
    Thus if array[index] != array[correct_index] with
    correct_index = array[i] - 1, we swap
    """
    i = 0
    while i < len(array):
        j = array[i] - 1
        if array[i] != array[j]:
            print(f"{array[i]} != {array[j]}")
            array[i], array[j] = array[j], array[i]
        else:
            i += 1
    print(array)
    return array


class CyclicSortTest(unittest.TestCase):
    def test_cyclic_sort(self):
        array = [5, 2, 3, 1, 4]
        self.assertEqual(cyclic_sort(array), sorted(array))
        array = [5, 4, 3, 2, 1]
        self.assertEqual(cyclic_sort(array), sorted(array))


if __name__ == "__main__":
    unittest.main()


```



#### [ insertion.py ]( insertion.py )

```python

import unittest

# O(n^2) time | O(1)) space
def insertion_sort(array):
    """The idea is to take the first element of the array as
    the first pivot and compare that element to the next element
    and see how we can insert that element on the left side of the pivot.
    So we take element on the right side of the pivot and insert them on
    the left side of the pivot at the right position
    """
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        array = [8, 5, 2, 9, 5, 6, 3]
        self.assertEqual(insertion_sort(array), sorted(array))


if __name__ == "__main__":
    unittest.main()


```



#### [ selection.py ]( selection.py )

```python

import unittest


# O(n^2) space | O(1) space
def selection_sort(array):
    """The idea is to keep a list (selection) of sorted element
    by searching for the smallest element from the current index
    and swapping it with the current index. Once done, we just
    have to increment the current index and do the previous operations
    again
    """
    cur_idx = 0
    while cur_idx < len(array) - 1:
        smallest_idx = cur_idx
        # search for smallest element
        for i in range(cur_idx + 1, len(array)):
            if array[i] < array[smallest_idx]:
                smallest_idx = i
        # swap element
        array[cur_idx], array[smallest_idx] = array[smallest_idx], array[cur_idx]
        cur_idx += 1

    return array


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        array = [8, 5, 2, 9, 5, 6, 3]
        self.assertEqual(selection_sort(array), sorted(array))


if __name__ == "__main__":
    unittest.main()


```



