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