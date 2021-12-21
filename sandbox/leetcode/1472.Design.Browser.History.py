import unittest


class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class BrowserHistory:
    def __init__(self, url) -> None:
        node = Node(url)
        self.head = node
        self.cur = node
        self.tail = node

    def __repr__(self):
        return f"{self.cur}"

    # O(1) time | O(1) space
    def visit(self, url):
        node = Node(url, None, self.cur)
        self.cur = node
        self.tail.next = node
        self.tail = node

    # O(s) time with s = number steps | O(1) space
    def forward(self, steps):
        cur = self.cur
        while cur.next:
            if steps == 0:
                break
            steps -= 1
            cur = cur.next
        self.cur = cur
        return cur.val

    # O(s) time with s = number steps | O(1) space
    def back(self, steps):
        cur = self.cur
        while cur.prev:
            if steps == 0:
                break
            steps -= 1
            cur = cur.prev
        self.cur = cur
        return cur.val


class TestBrowserHistory(unittest.TestCase):
    def test_history(self):
        bh = BrowserHistory("leetcode.com")
        for url in ("google.com", "facebook.com", "youtube.com"):
            bh.visit(url)
        print(bh)
        self.assertEqual(bh.back(1), "facebook.com")
        print(bh)
        self.assertEqual(bh.back(1), "google.com")
        print(bh)
        self.assertEqual(bh.forward(1), "facebook.com")
        print(bh)
        bh.visit("linkedin.com")
        print(bh)
        self.assertEqual(bh.forward(2), "linkedin.com")
        print(bh)
        self.assertEqual(bh.back(2), "google.com")
        print(bh)
        self.assertEqual(bh.back(7), "leetcode.com")
        print(bh.head)


if __name__ == "__main__":
    unittest.main()
