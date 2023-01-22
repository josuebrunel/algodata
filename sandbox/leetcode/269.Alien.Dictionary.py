import collections
import unittest


def letters_order(words):
    adj = {c: set() for w in words for c in w}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""

        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    res, visit = [], set()

    def dfs(c):
        if c in visit:
            return True

        visit.add(c)
        for n in adj[c]:
            if dfs(n):
                return True
        res.append(c)

    for c in adj:
        if c not in visit:
            if dfs(c):
                return ""

    return "".join(res[::-1])


class AlienDictionaryTest(unittest.TestCase):

    def test_letters_order(self):
        self.assertEqual(letters_order(["wrt", "wrf", "er", "ett", "rftt"]),
                         "wertf")
        self.assertEqual(letters_order(["z", "x"]), "zx")
        self.assertEqual(letters_order(["z", "x", "z"]), "")


if __name__ == "__main__":
    unittest.main()
