import unittest


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Stack:
    def __init__(self):
        self.head = None
        self._length = 0
        self.min_max = None

    def __repr__(self):
        return f"{self.head}"

    def __len__(self):
        return self._length

    def push(self, val):
        node = Node(val, self.head)
        self.head = node
        if not self.min_max:
            self.min_max = Node((val, val))
        else:
            new_min = min(val, self.min_max.val[0])
            new_max = max(val, self.min_max.val[1])
            min_max = Node((new_min, new_max), self.min_max)
            self.min_max = min_max
        self._length += 1

    def peek(self):
        return self.head.val

    def pop(self):
        val = self.head.val
        self.head = self.head.next
        self.min_max = self.min_max.next
        self._length -= 1
        return val

    def get_min(self):
        return self.min_max[0]

    def get_max(self):
        return self.min_max[1]


class TestStack(unittest.TestCase):
    def test_push(self):
        q = Stack()
        q.push(1)
        q.push(2)
        q.push(3)
        print(q)
        self.assertEqual(len(q), 3)
        self.assertEqual(q.head.val == 3, True)

    def test_peek(self):
        q = Stack()
        q.push(1)
        q.push(2)
        q.push(3)
        print(q)
        self.assertEqual(len(q), 3)
        self.assertEqual(q.peek() == 3, True)

    def test_pop(self):
        q = Stack()
        q.push(1)
        q.push(2)
        q.push(3)
        print(q)
        self.assertEqual(len(q), 3)
        self.assertEqual(q.pop() == 3, True)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.peek() == 2, True)

    def test_min_max(self):
        s = Stack()
        s.push(1)
        print(s, s.min_max)
        self.assertEqual(s.min_max.val == (1, 1), True)
        s.push(4)
        print(s, s.min_max)
        self.assertEqual(s.min_max.val == (1, 4), True)
        s.push(-1)
        print(s, s.min_max)
        self.assertEqual(s.min_max.val == (-1, 4), True)
        s.push(6)
        print(s, s.min_max)
        self.assertEqual(s.min_max.val == (-1, 6), True)
        s.pop()
        print(s, s.min_max)
        self.assertEqual(s.min_max.val == (-1, 4), True)
        s.pop()
        print(s, s.min_max)
        self.assertEqual(s.min_max.val == (1, 4), True)


if __name__ == "__main__":
    unittest.main()
