import unittest
import collections


def find_all_anagrams(s, p):
    slen, plen = len(s), len(p)
    pcount = collections.Counter(p)
    scount = collections.Counter(s[:plen])
    res = [0] if scount == pcount else []
    i = 0
    for j in range(plen, slen):
        scount[s[j]] = scount.get(s[j], 0) + 1
        scount[s[i]] -= 1
        if scount[s[i]] <= 0:
            scount.pop(s[i])
        i += 1
        if scount == pcount:
            res.append(i)
    return res


class FindAllAnagramsTest(unittest.TestCase):

    def test_find_all_anagram(self):
        self.assertCountEqual(find_all_anagrams("cbaebabacd", "abc"), [0, 6])
        self.assertCountEqual(find_all_anagrams("abab", "ab"), [0, 1, 2])
        self.assertCountEqual(find_all_anagrams("baa", "aa"), [1])


if __name__ == "__main__":
    unittest.main()
