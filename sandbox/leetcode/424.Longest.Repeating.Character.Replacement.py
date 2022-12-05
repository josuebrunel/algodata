import unittest


def character_replacement(s, k):
    L, R = 0, 0
    res = 0
    counter = {}
    for R in range(len(s)):
        counter[s[R]] = counter.get(s[R], 0) + 1
        if (R - L + 1) - max(counter.values()) > k:
            counter[s[L]] -= 1
            L += 1

        res = max(res, R - L + 1)

    return res


class LongestRepeatingCharacterReplacement(unittest.TestCase):

    def test_character_replacement(self):
        self.assertEqual(character_replacement("ABAB", 2), 4)
        self.assertEqual(character_replacement("AABABBA", 1), 4)


if __name__ == "__main__":
    unittest.main()
