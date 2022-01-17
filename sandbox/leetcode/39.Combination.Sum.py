import unittest


# O(2*t) time where t is the target value | O(t) space
def combination_sum(candidates, target):
    res = []
    backtrack(target, candidates, 0, [], res)
    return res


def backtrack(target, candidates, cur, choices, res):
    print(cur, choices)
    csum = sum(choices)
    if cur >= len(candidates) or csum > target:
        return
    if csum == target:
        if choices not in res:
            print("FOUND: ", choices)
            res.append(choices.copy())

    choices.append(candidates[cur])
    backtrack(target, candidates, cur, choices, res)
    choices.pop()
    backtrack(target, candidates, cur + 1, choices, res)


class CombinationSumTest(unittest.TestCase):
    def test_combination_test(self):
        self.assertEqual(combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(
            combination_sum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        )


if __name__ == "__main__":
    unittest.main()
