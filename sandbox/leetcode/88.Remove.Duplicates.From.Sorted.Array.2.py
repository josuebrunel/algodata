import unittest


def remove_duplicates(array):
    """The idea is to use a 2 pointers approach
    one pointer (i) to iterate over the array and
    another pointer (j) that's increased only when
    array[i] is different from array[j-2].
    Just as for remove duplicates (I), as long as
    values are the same we do nothing
    """
    j = 2
    for i in range(2, len(array)):
        if array[i] != array[j - 2]:
            array[j] = array[i]
            j += 1
    return j


class RemoveDuplicateTest(unittest.TestCase):
    def test_remove_duplicates(self):
        array = [1, 1, 1, 2, 2, 3]
        self.assertEqual(array[: remove_duplicates(array)], [1, 1, 2, 2, 3])
        array = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        self.assertEqual(array[: remove_duplicates(array)], [0, 0, 1, 1, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
