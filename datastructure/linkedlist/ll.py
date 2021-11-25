class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f"{self.head}"

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        size = 0
        head = self.head
        while head:
            size += 1
            head = head.next
        return size

    def append(self, val):
        node = Node(val)
        head = self.head
        while head.next:
            head = head.next
        head.next = node

    def insert_at(self, val, pos):
        head = self.head
        prev = None
        while head:
            if pos == 0:
                break
            prev = head
            head = head.next
            pos -= 1
        node = Node(val)
        prev.next = node
        node.next = head

    def remove(self, val):
        cur = self.head
        prev = None
        while cur.next:
            if cur.val == val:
                break
            prev = cur
            cur = cur.next
        prev.next = cur.next

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        self.head = prev


if __name__ == "__main__":
    head = Node(1)
    ll = LinkedList(head)
    print(len(ll))
    ll.append(2)
    ll.append(3)
    size = len(ll)
    print(size)
    assert size == 3
    print(ll)
    ll.append(5)
    print(ll)
    ll.insert_at(4, 3)
    print(ll)
    ll.remove(4)
    print(ll)
    ll.reverse()
    print(ll)
    assert ll.head.val == 5
