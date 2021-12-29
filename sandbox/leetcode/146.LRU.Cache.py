import unittest


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"({self.key}|{self.val}) -> {self.next}"


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.lru = None
        self.mru = None

    def __repr__(self):
        return f"{self.lru}"

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        if nxt:
            nxt.prev = prev
        if prev:
            prev.next = nxt

    def _add(self, node):
        node.prev = self.mru
        self.mru.next = node
        self.mru = node

    def get(self, key):
        # if key not in cache we return -1
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # if node is mru we do nothing
        if self.mru == node:
            pass
        # if node is lru, we set lru as lru.next
        # and node as the new mru
        elif self.lru == node:
            self.lru = node.next
            self.lru.prev = None
            node.prev = self.mru
            self.mru.next = node
            self.mru = node
        # else we just set node as the new mru
        else:
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev
            node.prev = self.mru
            self.mru.next = node
            self.mru = node

        return node.val

    def put(self, key, value):
        node = Node(key, value)
        # if no entry we set lru and mru to new node
        if not self.lru:
            self.lru = node
            self.mru = node
        # if cap is full
        # we remove lru from the cache and set next element
        # to lru (lru.next) as new lru
        # then add new element as new mru
        elif len(self.cache) == self.cap:
            lru = self.lru
            self.cache.pop(lru.key)
            self.lru = lru.next
            mru = self.mru
            mru.next = node
            node.prev = mru
            self.mru = node
        # otherwise we add new element as our new mru
        else:
            self._add(node)

        self.cache[key] = node


class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        lru = LRUCache(2)
        print(lru)
        lru.put(1, 1)
        lru.put(2, 2)
        print(lru)
        self.assertEqual(lru.get(1), 1)
        lru.put(3, 3)
        print(lru)
        self.assertEqual(lru.get(2), -1)
        lru.put(4, 4)
        print(lru)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(3), 3)
        print(lru)
        self.assertEqual(lru.get(4), 4)
        print(lru)


if __name__ == "__main__":
    unittest.main()
