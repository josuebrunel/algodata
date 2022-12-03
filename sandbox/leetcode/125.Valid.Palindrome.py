import unittest


def valid_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


class ValidPalindromeTest(unittest.TestCase):

    def test_valid_palindrom(self):
        self.assertEqual(valid_palindrome("A man, a plan, a canal: Panama"),
                         True)
        self.assertEqual(valid_palindrome("race a car"), False)
        self.assertEqual(valid_palindrome(" "), True)


if __name__ == "__main__":
    unittest.main()
