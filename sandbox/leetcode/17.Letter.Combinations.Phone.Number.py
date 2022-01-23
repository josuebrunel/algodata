import unittest

# O(4^n) time where 4 is the max number of letter for 1 digit
# O(n) space where n is the length of digits
def letter_combinations(digits):
    keypad = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    if not digits:
        return []
    res = []
    backtrack(keypad, digits, 0, [], res)
    return res


def backtrack(keypad, digits, pos, comb, res):
    if len(comb) == len(digits):
        print(comb)
        res.append("".join(comb.copy()))
        return

    for i in keypad[digits[pos]]:
        comb.append(i)
        backtrack(keypad, digits, pos + 1, comb, res)
        comb.pop()


class LetterCombinationsTest(unittest.TestCase):
    def test_letter_combinations(self):
        digits = "23"
        result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(letter_combinations(digits), result)
        digits = ""
        result = []
        self.assertEqual(letter_combinations(digits), result)
        digits = "2"
        result = ["a", "b", "c"]
        self.assertEqual(letter_combinations(digits), result)


if __name__ == "__main__":
    unittest.main()
