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
