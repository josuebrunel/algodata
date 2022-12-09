import unittest


def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return True if i == len(s) else False


class IsSubsequenceTest(unittest.TestCase):

    def test_is_subsequence(self):
        self.assertEqual(is_subsequence("abc", "ahbgdc"), True)
        self.assertEqual(is_subsequence("axc", "ahbgdc"), False)


if __name__ == "__main__":
    unittest.main()
