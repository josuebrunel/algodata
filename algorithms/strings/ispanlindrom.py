import unittest
import string


def is_palindrom(s):
    allowed = set(string.ascii_lowercase + string.digits)
    s = [c for c in s.lower() if c in allowed]
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

class TestIsPalindrom(unittest.TestCase):

    def test_is_palindrom(self):
        self.assertEqual(True, is_palindrom("A man, a plan, a canal: Panama"))
        self.assertEqual(False, is_palindrom("race a car"))

if __name__ == "__main__":
    unittest.main()