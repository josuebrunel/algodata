import unittest
import collections


def check_inclusion(s, p):
    slen = len(s)
    scount = collections.Counter(s)
    pcount = collections.Counter(p[:slen])
    if scount == pcount:
        return True
    L = 0
    for R in range(slen, len(p)):
        pcount[p[R]] = pcount.get(p[R], 0) + 1
        pcount[p[L]] -= 1
        if pcount[p[L]] <= 0:
            pcount.pop(p[L])

        if pcount == scount:
            return True
        L += 1

    return False


class PermutationInString(unittest.TestCase):

    def test_permutation(self):
        self.assertEqual(check_inclusion("ab", "eidbaooo"), True)
        self.assertEqual(check_inclusion("ab", "eidboaoo"), False)


if __name__ == "__main__":
    unittest.main()
