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
