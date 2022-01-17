import unittest


def remove_duplicates(array):
    j = 1

    for i in range(1, len(array)):

        if array[i] != array[i - 1]:
            array[j] = array[i]
            j += 1
    return j


class RemoveDuplicateTest(unittest.TestCase):
    def test_remove_duplicates(self):
        array = [1, 1, 2]
        self.assertEqual(array[: remove_duplicates(array)], array[:2])
        array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(array[: remove_duplicates(array)], array[:5])


if __name__ == "__main__":
    unittest.main()
