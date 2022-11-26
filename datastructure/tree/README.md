[bst.py](#-bstpy-)
[trie.py](#-triepy-)
#### [ bst.py ]( bst.py )

```python

import unittest


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.value} [{self.left}, {self.right}]"

    def insert(self, val):
        if not self.value:
            self.value = val
            return True
        if val < self.value:
            if self.left:
                return self.left.insert(val)
            self.left = Node(val)
        else:
            if self.right:
                return self.right.insert(val)
            self.right = Node(val)
        return True

    def find(self, val):
        if self.value < val:
            if not self.right:
                return False
            return self.right.find(val)
        elif self.value > val:
            if not self.left:
                return False
            return self.left.find(val)
        else:
            return True

    def findMin(self, node=False):
        cur = self
        while cur.left:
            cur = cur.left
        return cur.value if not node else cur

    def findMax(self, node=False):
        cur = self
        while cur.right:
            cur = cur.right
        return cur.value if not node else cur

    def remove(self, val):
        if self.value > val:
            if not self.left:
                return self
            self.left = self.left.remove(val)
        elif self.value < val:
            if not self.right:
                return self
            self.right = self.right.remove(val)
        else:
            if not self.right:
                return self.left
            elif not self.left:
                return self.right
            else:
                leftMaxNode = self.findMax(self.left)
                self.val = leftMaxNode.value
                self.left = self.left.remove(leftMaxNode.value)
        return self

    def inorder(self):
        values = []
        stack = []
        current = self
        while current or stack:
            if current:
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                values.append(current.value)
                current = current.left
        return values


class BSTTest(unittest.TestCase):

    def test_bst(self):
        root = Node(5)
        root.insert(3)
        root.insert(7)
        print(root)
        self.assertEqual(root.find(7), True)
        self.assertEqual(root.find(17), False)
        root.insert(2)
        print(root)
        self.assertEqual(root.find(2), True)
        self.assertEqual(root.findMin(), 2)
        self.assertEqual(root.findMax(), 7)
        root.insert(6)
        root.insert(4)
        print(root)
        root.remove(6)
        print(root)
        self.assertEqual(root.find(6), False)
        root.remove(5)
        print(root)
        self.assertEqual(root.find(5), False)


if __name__ == "__main__":
    unittest.main()


```



#### [ trie.py ]( trie.py )

```python

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


```



