* [isanagram.py](#-isanagrampy-)
* [ispanlindrom.py](#-ispanlindrompy-)
* [longestpalindromicsubstring.py](#-longestpalindromicsubstringpy-)
#### [ isanagram.py ]( isanagram.py )

```python

import unittest


def is_anagram(a, b):
    if len(a) != len(b):
        return False
    counter = {}
    for i in range(len(a)):
        counter[a[i]] = counter.get(a[i], 0) + 1
        counter[b[i]] = counter.get(b[i], 0) - 1
    for v in counter.values():
        if v != 0:
            return False
    return True


class TestIsAnagram(unittest.TestCase):

    def test_is_anagram(self):
        self.assertEqual(False, is_anagram("a", "ab"))
        self.assertEqual(True, is_anagram("anagram", "nagaram"))
        self.assertEqual(False, is_anagram("car", "cat"))


if __name__ == "__main__":
    unittest.main()

```



#### [ ispanlindrom.py ]( ispanlindrom.py )

```python

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

```



#### [ longestpalindromicsubstring.py ]( longestpalindromicsubstring.py )

```python

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

```



