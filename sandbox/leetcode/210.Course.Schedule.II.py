import unittest

# O(E+V) time where E = Prerequesites and V number of courses
#
def find_order(num, prerequisites):
    pre_map = {i: [] for i in range(num)}
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)

    visit = [0 for _ in range(num)]
    order = []

    def dfs(crs):
        if visit[crs] == -1:
            return False
        if visit[crs] == 1:
            return True

        visit[crs] = -1
        for pre in pre_map[crs]:
            if not dfs(pre):
                return False
        visit[crs] = 1
        order.append(crs)
        return True

    for i in range(num):
        if not dfs(i):
            return []
    print(order)
    return order


class FindOrderTest(unittest.TestCase):
    def test_find_order(self):
        self.assertEqual(find_order(2, [[1, 0]]), [0, 1])
        self.assertEqual(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 1, 2, 3])
        self.assertEqual(find_order(1, []), [0])


if __name__ == "__main__":
    unittest.main()
