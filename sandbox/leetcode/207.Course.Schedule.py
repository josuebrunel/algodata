import unittest

from collections import deque, defaultdict


def can_finish(num, prerequisites):
    # we create an adjacent list mapping
    # courses and their prereq
    pre_map = {i: [] for i in range(num)}
    # now we populate this map
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)

    # we define a set to track the visited courses
    visited = set()

    def dfs(crs):
        # check if cycle
        if crs in visited:
            return False
        # if crs don't have prerequisites
        # it can be finished
        if not pre_map[crs]:  # empty list
            return True

        visited.add(crs)
        for pre in pre_map[crs]:
            if not dfs(pre):
                return False
        visited.remove(crs)
        # since this course can be finished
        # we can remove all its dependancies
        pre_map[crs] = []
        return True

    for i in range(num):
        if not dfs(i):
            return False
    return True


class CourseScheduleTest(unittest.TestCase):
    def test_can_finish(self):
        self.assertEqual(can_finish(2, [[1, 0]]), True)
        self.assertEqual(can_finish(2, [[1, 0], [0, 1]]), False)


if __name__ == "__main__":
    unittest.main()
