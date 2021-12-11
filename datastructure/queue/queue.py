import unittest


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __repr__(self):
        return f"{self.head}"

    def __len__(self):
        return self._length

    def enqueue(self, val):
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            node = Node(val)
            self.tail.next = node
            self.tail = node
        self._length += 1

    def dequeue(self):
        if not self.head:
            return
        val = self.head.val
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        self._length -= 1
        return val


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        print(q)
        self.assertEqual(len(q), 3)
        self.assertEqual(q.head.val == 1, True)
        self.assertEqual(q.tail.val == 3, True)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        print(q, "\n")
        self.assertEqual(q.dequeue() == 1, True)
        self.assertEqual(q.dequeue() == 2, True)
        self.assertEqual(len(q) == 1, True)
        self.assertEqual(q.head, q.tail)
        print(q)


if __name__ == "__main__":
    unittest.main()
