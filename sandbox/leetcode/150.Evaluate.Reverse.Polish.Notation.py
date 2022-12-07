import unittest


def evalRPN(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))

    return stack[0]


class ReversePolishNotationTest(unittest.TestCase):

    def test_evalRPN(self):
        self.assertEqual(evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(
            evalRPN([
                "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5",
                "+"
            ]), 22)


if __name__ == "__main__":
    unittest.main()
