import unittest


class Node:

    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True

    def search(self, word):

        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end

        return dfs(0, self.root)


class WordDictionaryTest(unittest.TestCase):

    def test_word_dictionary(self):
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        self.assertEqual(wd.search("pad"), False)
        self.assertEqual(wd.search("bad"), True)
        self.assertEqual(wd.search(".ad"), True)
        self.assertEqual(wd.search("b.."), True)
        wd = WordDictionary()
        wd.addWord("a")
        wd.addWord("a")
        self.assertEqual(wd.search("."), True)
        self.assertEqual(wd.search("a"), True)
        self.assertEqual(wd.search("aa"), False)
        self.assertEqual(wd.search("a"), True)
        self.assertEqual(wd.search(".a"), False)
        self.assertEqual(wd.search("a."), False)


if __name__ == "__main__":
    unittest.main()
