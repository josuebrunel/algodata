import unittest


class Node:

    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end

    def prefix(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


class TrieTest(unittest.TestCase):

    def test_trie(self):
        trie = Trie()
        trie.add("hello")
        trie.add("daddy")
        trie.add("bad")
        self.assertEqual(trie.search("Hello"), False)
        self.assertEqual(trie.search("hello"), True)
        self.assertEqual(trie.prefix("dad"), True)


if __name__ == "__main__":
    unittest.main()
