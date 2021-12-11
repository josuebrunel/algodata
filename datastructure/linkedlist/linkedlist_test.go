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
