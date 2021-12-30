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
