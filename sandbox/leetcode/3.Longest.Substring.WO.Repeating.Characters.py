import unittest


def lenOfLongestSubstring(s):
    res, L = 0, 0
    css = set()
    for R in range(len(s)):
        while s[R] in css:
            css.remove(s[L])
            L += 1
        css.add(s[R])
        res = max(res, R - L + 1)
    return res


class LongestSubstringWORepeatingChrs(unittest.TestCase):

    def test_longest_substring_wo_repeating_chars(self):
        self.assertEqual(lenOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lenOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lenOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
