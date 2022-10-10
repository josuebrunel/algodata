import unittest

from collections import Counter


def count_students(students, sandwiches):
    counter = Counter(students)

    for i in sandwiches:
        if counter[i] == 0:
            break
        counter[i] -= 1

    return counter.total()


class CountStudentsTest(unittest.TestCase):

    def count_students(self):
        self.assertEqual(count_students([1, 1, 0, 0], [0, 1, 0, 1]), 0)
        self.assertEqual(
            count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), 3)
        self.assertEqual(count_students([1, 1], [1, 0]), 2)


if __name__ == "__main__":
    unittest.main()
