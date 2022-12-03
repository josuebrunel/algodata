* [linkedlist.py](#-linkedlistpy-)
* [linkedlist_test.go](#-linkedlist_testgo-)
#### [ linkedlist.py ]( linkedlist.py )

```python

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


```



#### [ linkedlist_test.go ]( linkedlist_test.go )

```golang

package linkedlist

import (
	"fmt"
	"testing"
)

// Node represents a node of a linked list
type Node struct {
	val  int
	next *Node
}

// String representation of a node
func (n Node) String() string {
	return fmt.Sprintf("%d -> ", n.val)
}

// LinkedList represents a sequence nodes
type LinkedList struct {
	head   *Node
	length int
}

// Prepend add a new node at the beginning of the linked list
func (ll *LinkedList) Prepend(val int) {
	node := &Node{val, ll.head}
	ll.head = node
	ll.length++
}

// Append add a new now at the end of the linked list
func (ll *LinkedList) Append(val int) {
	if ll.head == nil {
		ll.head = &Node{val: val}
		ll.length++
		return
	}
	cur := ll.head
	for cur.next != nil {
		cur = cur.next
	}
	cur.next = &Node{val: val}
	ll.length++
}

func (ll *LinkedList) InsertAt(val, pos int) {
	if ll.head == nil {
		ll.head = &Node{val, nil}
		ll.length++
		return
	}
	cur := ll.head
	var prev *Node
	for cur != nil {
		if pos == 0 {
			break
		}
		prev = cur
		cur = cur.next
		pos--
	}
	prev.next = &Node{val, cur}
	ll.length++
}

func (ll *LinkedList) Remove(val int) {
	if ll == nil {
		return
	}
	cur := ll.head
	var prev *Node
	for cur != nil {
		if cur.val == val {
			break
		}
		prev = cur
		cur = cur.next
	}
	prev.next = cur.next
	ll.length--
}

func (ll *LinkedList) Reverse() {
	if ll.head == nil {
		return
	}
	var prev *Node
	cur := ll.head
	for cur != nil {
		nextNode := cur.next
		cur.next = prev
		prev = cur
		cur = nextNode
	}
	ll.head = prev
}

func TestPrepend(t *testing.T) {
	ll := LinkedList{}
	ll.Prepend(1)
	ll.Prepend(0)
	if ll.head.val != 0 {
		t.Fatal("Unexpected value")
	}
}

func TestAppend(t *testing.T) {
	ll := LinkedList{}
	ll.Append(1)
	ll.Append(2)
	ll.Append(3)
	if ll.length != 3 {
		t.Fatalf("Unexpected length (%d)", ll.length)
	}
}

func TestInsertAt(t *testing.T) {
	ll := LinkedList{}
	ll.Append(1)
	ll.Append(2)
	ll.Append(3)
	ll.Append(5)
	ll.InsertAt(4, 3)
	if ll.length != 5 {
		t.Fatalf("Unexpected length (%d)", ll.length)
	}
}

func TestRemove(t *testing.T) {
	ll := LinkedList{}
	ll.Append(1)
	ll.Append(2)
	ll.Append(3)
	ll.Append(4)
	ll.Append(5)
	ll.Remove(4)
	if ll.length != 4 {
		t.Fatalf("Unexpected length (%d)", ll.length)
	}
}

func TestReverse(t *testing.T) {
	ll := LinkedList{&Node{1, nil}, 1}
	for i := 1; i < 6; i++ {
		ll.Append(i)
	}
	if ll.head.val != 1 {
		t.Fatalf("Invalid head val (%d)", ll.head.val)
	}
	ll.Reverse()
	if ll.head.val != 5 {
		t.Fatalf("Invalid head val (%d)", ll.head.val)
	}
}


```



