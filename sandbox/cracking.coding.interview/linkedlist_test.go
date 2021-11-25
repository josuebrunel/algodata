package linkedlist

import (
	"fmt"
	"testing"
)

type Node struct {
	next *Node
	val  int
}

func (n Node) Print() {
	fmt.Printf("%v\n", n)
}

type LinkedList struct {
	head   *Node
	length int
}

func (l LinkedList) Print() {
	head := l.head
	for l.length != 0 {
		fmt.Printf("%d ", head.val)
		head = head.next
		l.length--
	}
	fmt.Println()
}

func (l *LinkedList) Prepend(n *Node) {
	cHead := l.head
	l.head = n
	n.next = cHead
	l.length++
}

func (l *LinkedList) Append(n *Node) {
	head := l.head
	for head.next != nil {
		head = head.next
	}
	head.next = n
	l.length++
}

func (l LinkedList) GetByValue(v int) *Node {
	head := l.head
	for head.val != v {
		if head.next == nil {
			return &Node{}
		}
		head = head.next
	}
	return head
}

func (l *LinkedList) DeleteByValue(v int) {
	head := l.head
	if head.val == v {
		l.head = head.next
		l.length--
		return
	}
	prev := head
	for prev.next.val != v {
		if prev.next.next == nil {
			return
		}
		prev = prev.next
	}
	prev.next = prev.next.next
	l.length--
	return
}

func (l *LinkedList) RemoveDuplicate() *LinkedList {
	head := l.head

	for head.next != nil {
		if head.val != head.next.Val {
			continue
		}
	}
}

func TestHelloWorld(t *testing.T) {
	l := LinkedList{}
	node1 := Node{nil, 1}
	node2 := Node{&node1, 2}
	node3 := Node{&node2, 3}
	l.Prepend(&node1)
	l.Prepend(&node2)
	l.Prepend(&node3)
	l.Print()
	if l.length != 3 {
		t.Errorf("LinkedList length != 3")
	}
	node4 := Node{nil, 4}
	l.Append(&node4)
	l.Print()
	if l.length != 4 {
		t.Errorf("Expected length is 4")
	}
	n := l.GetByValue(1)
	n.Print()
	if n.val != 1 && n.next != &node4 {
		t.Errorf("Node value different from 1")
	}
	n = l.GetByValue(10)
	if n.val != 0 && n.next != nil {
		t.Errorf("Node should be empty")
	}
	node10 := Node{nil, 10}
	node13 := Node{nil, 13}
	node7 := Node{nil, 7}
	l.Append(&node10)
	l.Append(&node7)
	l.Append(&node13)
	l.Print()
	if l.length != 7 {
		t.Errorf("Expected length is 7")
	}
	l.DeleteByValue(3)
	l.Print()
	if l.length != 6 {
		t.Errorf("Expected length is 6 but %d found", l.length)
	}
	l.DeleteByValue(10)
	l.Print()
	if l.length != 5 {
		t.Errorf("Expected length is 5 but %d found", l.length)
	}
}
