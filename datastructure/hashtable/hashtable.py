import unittest


class Node:
    def __init__(self, key, val=None, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f"{self.key} -> {self.next}"


class Bucket:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f"({self.head})"

    def insert(self, key, val=None):
        if self.search(key):
            return
        node = Node(key, val, nxt=self.head)
        self.head = node

    def search(self, key):
        if not self.head:
            return
        cnode = self.head
        while cnode:
            if cnode.key == key:
                break
            cnode = cnode.next
        if not cnode:
            return
        return cnode.val

    def delete(self, key):
        if not self.head:
            return
        if self.head.key == key:
            self.head = self.head.next
            return
        cnode = self.head
        prev = None
        while cnode:
            if cnode.key == key:
                break
            prev = cnode
            cnode = cnode.next
        prev.next = cnode.next


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.array = []
        for _ in range(self.size):
            self.array.append(Bucket())

    def __repr__(self):
        return f"{self.array}"

    def xhash(self, key):
        return sum([ord(c) for c in str(key)]) % self.size

    def put(self, key, val):
        index = self.xhash(key)
        self.array[index].insert(key, val)

    def get(self, key):
        index = self.xhash(key)
        return self.array[index].search(key)

    def remove(self, key):
        index = self.xhash(key)
        return self.array[index].delete(key)


class TestHashTable(unittest.TestCase):
    def test_hasttable(self):
        h = HashTable(10)
        h.put("josh", {"age": 32})
        h.put("josh", "someone")
        h.put(10, "dix")
        h.put("cat", "pet")
        h.put("tac", "sweet")
        print(h)
        self.assertEqual(h.get("josh"), {"age": 32})
        self.assertEqual(h.get(10), "dix")
        self.assertEqual(h.get("cat"), "pet")
        h.remove("cat")
        print(h)
        self.assertEqual(h.get("cat"), None)
        self.assertEqual(h.get("tac"), "sweet")


if __name__ == "__main__":
    unittest.main()
