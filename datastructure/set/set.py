import unittest


class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Set:
    def __init__(self):
        self.mod = 10
        self.elements = [None for _ in range(self.mod)]
        self.length = 0

    def __len__(self):
        return self.length

    def _lookup(self, val):
        idx = sum([ord(c) for c in str(val)]) % self.mod
        return idx

    def add(self, val):
        idx = self._lookup(val)
        head = self.elements[idx]
        if not head:
            self.elements[idx] = Node(val)
        elif head.val == val:
            return
        else:
            while head.next:
                head = head.next
            head.next = Node(val)
        self.length += 1

    def exists(self, val):
        idx = self._lookup(val)
        head = self.elements[idx]
        if not head:
            return False
        if head.val == val:
            return True

        while head:
            if head.val == val:
                return True
            head = head.next
        return False

    def remove(self, val):
        idx = self._lookup(val)
        head = self.elements[idx]
        if not head:
            return
        if head.val == val:
            head = head.next
        else:
            node = head
            while node.next:
                if node.next.val == val:
                    node.next = node.next.next
                    break
                head = node.next
        self.elements[idx] = head
        self.length -= 1


class SetTestCase(unittest.TestCase):
    def test_set(self):
        s = Set()
        for i in range(5):
            s.add(i)
        # test add
        self.assertEqual(len(s), 5)
        # test exist
        self.assertEqual(s.exists(3), True)
        self.assertEqual(s.exists(1), True)
        self.assertEqual(s.exists(5), False)
        # test remove
        s.remove(3)
        self.assertEqual(s.exists(3), False)
        self.assertEqual(len(s), 4)
        s.remove(1)
        self.assertEqual(s.exists(1), False)
        self.assertEqual(len(s), 3)
        s.remove(4)
        self.assertEqual(s.exists(4), False)
        self.assertEqual(len(s), 2)


if __name__ == "__main__":
    unittest.main()
