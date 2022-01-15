import unittest


def generate_parenthesis(n):
    # The idea is to backtrack the number of open and closed parenthesis
    # if openN == closedN == n we return the stack and append it to the result
    # if openN < n we add a new open parenthesis
    # if closedN < openN we add a closed parenthesis
    # with openN the counter of open parenthesis
    # and closedN the counter of closed parenthesis
    res = []
    stack = []
    backtrack(0, 0, n, res, stack)
    return res


def backtrack(ob, cb, n, res, stack):
    if ob == cb == n:
        res.append("".join(stack))
    if ob < n:
        stack.append("(")
        backtrack(ob + 1, cb, n, res, stack)
        stack.pop()
    if cb < ob:
        stack.append(")")
        backtrack(ob, cb + 1, n, res, stack)
        stack.pop()


class TestGenerateParenthesis(unittest.TestCase):
    def test_generate_parenthesis(self):
        self.assertEqual(generate_parenthesis(1), ["()"])
        res = generate_parenthesis(3)
        self.assertIn("((()))", res)
        self.assertIn("(()())", res)
        self.assertIn("(())()", res)
        self.assertIn("()(())", res)
        self.assertIn("()()()", res)


if __name__ == "__main__":
    unittest.main()
