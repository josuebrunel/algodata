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
