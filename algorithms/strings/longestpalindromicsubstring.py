import unittest


def longest_palindromic_substring(s):
    longest = [0, 1]
    for i in range(1, len(s)):
        odd = get_longest_palindromic(s, i-1, i)
        even = get_longest_palindromic(s, i-1, i+1)
        cur_longest = max(odd, even, key=lambda x: x[1] - x[0])
        longest = max(longest, cur_longest, key=lambda x: x[1] - x[0])
    return s[longest[0]:longest[1]]


def get_longest_palindromic(s, i, j):
    while i >= 0 and j < len(s):
        if s[i] != s[j]:
            break
        i -= 1
        j += 1
    return [i+1, j]


class TestLongestPalindromicSubstring(unittest.TestCase):

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")        
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")        
        self.assertEqual(longest_palindromic_substring("a"), "a")        
        self.assertEqual(longest_palindromic_substring("ac"), "a")        


if __name__ == "__main__":
    unittest.main()