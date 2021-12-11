import unittest


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f"{self.val}->{self.next}"


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f"{self.head}"

    def __len__(self):
        node = self.head
        counter = 0
        while node:
            counter += 1
            node = node.next
        return counter

    @staticmethod
    def from_list(array):
        if not array:
            return LinkedList()
        ll = LinkedList(Node(array[0]))
        node = ll.head
        for i in range(1, len(array)):
            node.next = Node(array[i])
            node = node.next
        return ll

    def to_list(self):
        array = []
        node = self.head
        while node:
            array.append(node.val)
            node = node.next
        return array

    # O(1)
    def prepend(self, val):
        node = Node(val, self.head)
        self.head = node

    # O(n)
    def append(self, val):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)

    # O(n)
    def insert_at(self, val, pos):
        node = self.head
        prev = None
        while node.next:
            if pos == 0:
                break
            prev = node
            node = node.next
            pos -= 1
        new_node = Node(val, node)
        prev.next = new_node

    # O(n)
    def remove(self, val):
        node = self.head
        prev = None
        while node.next:
            if node.val == val:
                break
            prev = node
            node = node.next
        prev.next = node.next

    # O(n)
    def reverse(self):
        node = self.head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        self.head = prev


class TestLinkedList(unittest.TestCase):
    def test_from_list(self):
        print("Test from list")
        ll = LinkedList.from_list([1, 2, 3, 4, 5])
        print(ll)
        self.assertEqual(len(ll) == 5, True)

    def test_prepend(self):
        print("Test prepend")
        ll = LinkedList.from_list([1, 2, 3, 4, 5])
        print(ll)
        ll.prepend(0)
        print(ll)
        self.assertEqual(len(ll) == 6, True)

    def test_append(self):
        print("Test append")
        ll = LinkedList.from_list([1, 2, 3, 4, 5])
        print(ll)
        ll.append(6)
        print(ll)
        self.assertEqual(len(ll) == 6, True)

    def test_insert_at(self):
        print("Test insert at")
        ll = LinkedList.from_list([1, 2, 3, 5])
        print(ll)
        ll.insert_at(4, 3)
        print(ll)
        self.assertEqual(len(ll) == 5, True)

    def test_remove(self):
        print("Test remove")
        ll = LinkedList.from_list([1, 2, 3, 4, 5])
        print(ll)
        ll.remove(4)
        print(ll)
        self.assertEqual(len(ll) == 4, True)

    def test_reverse(self):
        print("Test reverse")
        ll = LinkedList.from_list([1, 2, 3, 4, 5])
        print(ll)
        ll.reverse()
        print(ll)
        self.assertEqual(ll.to_list() == [5, 4, 3, 2, 1], True)


if __name__ == "__main__":
    unittest.main()
