import unittest


def permute(nums):
    res = []
    seen = set()

    def backtrack(perm):
        if len(perm) == len(nums):
            res.append(perm.copy())
            return

        for i in nums:
            if i in seen:
                continue

            perm.append(i)
            seen.add(i)
            backtrack(perm)
            perm.pop()
            seen.remove(i)

    backtrack([])
    return res


class PermutationsTest(unittest.TestCase):

    def test_permutations(self):
        self.assertCountEqual(
            permute([1, 2, 3]),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        self.assertCountEqual(permute([0, 1]), [[0, 1], [1, 0]])
        self.assertCountEqual(permute([1]), [[1]])


if __name__ == "__main__":
    unittest.main()
