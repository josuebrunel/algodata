import unittest
import collections


def group_anagrams(strs):
    res = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()


class GroupAnagramsTest(unittest.TestCase):

    def test_group_anagrams(self):
        self.assertCountEqual(
            group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
        self.assertCountEqual(group_anagrams([""]), [[]])
        self.assertCountEqual(group_anagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()
