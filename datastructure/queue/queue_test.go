package queue

import (
	"fmt"
	"testing"
)

// Node represents an element in a queue
type Node struct {
	val  int
	next *Node
}

// String is the string representation of a node
func (n Node) String() string {
	if n.next == nil {
		return fmt.Sprintf("%d -> nil", n.val)
	}
	return fmt.Sprintf("%d -> %s", n.val, n.next)
}

// Queue represents a sequence of nodes
type Queue struct {
	head   *Node
	tail   *Node
	length int
}

// Enqueue add an element to a queue
func (q *Queue) Enqueue(val int) {
	if q.head == nil {
		q.head = &Node{val, nil}
		q.tail = q.head
	} else {
		node := &Node{val, nil}
		q.tail.next = node
		q.tail = node
	}
	q.length++
}

// Dequeue pops an element from the queue
func (q *Queue) Dequeue() int {
	if q.head == nil {
		return -1
	}
	val := q.head.val
	q.head = q.head.next
	if q.head == nil {
		q.tail = nil
	}
	q.length--
	return val
}

func TestEnqueue(t *testing.T) {
	q := Queue{}
	for i := 1; i <= 5; i++ {
		q.Enqueue(i)
	}
	t.Logf("%s", q.head)
	if q.length != 5 {
		t.Fatalf("Unexpected length (%d)", q.length)
	}
	if q.head.val != 1 {
		t.Fatalf("Unexpected value (%d)", q.head.val)
	}
	if q.tail.val != 5 {
		t.Fatalf("Unexpected value (%d)", q.tail.val)
	}
}

func TestDequeue(t *testing.T) {
	q := Queue{}
	for i := 1; i <= 5; i++ {
		q.Enqueue(i)
	}
	t.Logf("%s", q.head)
	for i := 0; i < 4; i++ {
		q.Dequeue()
	}
	t.Logf("%s", q.head)
	if q.length != 1 {
		t.Fatalf("Unexpected length (%d)", q.length)
	}
	if q.head.val != 5 {
		t.Fatalf("Unexpected value (%d)", q.head.val)
	}
	if q.tail.val != 5 {
		t.Fatalf("Unexpected value (%d)", q.tail.val)
	}
}
