import unittest


def length_of_last_word(s):
    i = len(s) - 1
    length = 0

    while s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length


class LengthOfLastWord(unittest.TestCase):

    def test_length_of_last_word(self):
        self.assertEqual(length_of_last_word("Hello World"), 5)
        self.assertEqual(length_of_last_word("   fly me   to   the moon  "), 4)
        self.assertEqual(length_of_last_word("luffy is still joyboy"), 6)


if __name__ == "__main__":
    unittest.main()
