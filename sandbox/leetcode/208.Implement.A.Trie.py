import unittest


class Node:

    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
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

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


class TrieTest(unittest.TestCase):

    def test_trie(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.startsWith("app"), True)
        trie.insert("app")
        self.assertEqual(trie.search("app"), True)


if __name__ == "__main__":
    unittest.main()
