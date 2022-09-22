import unittest


def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    counter_s, counter_t = {}, {}

    for i in range(len(s)):
        counter_s[s[i]] = counter_s.get(s[i], 0) + 1
        counter_t[t[i]] = counter_t.get(t[i], 0) + 1

    return counter_s == counter_t


class ValidAnagramTest(unittest.TestCase):

    def test_valid_anagram(self):
        self.assertEqual(valid_anagram("anagram", "nagaram"), True)
        self.assertEqual(valid_anagram("rat", "car"), False)


if __name__ == "__main__":
    unittest.main()
