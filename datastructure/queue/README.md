[queue.py](#-queuepy-)
[queue_test.go](#-queue_testgo-)
#### [ queue.py ]( queue.py )

```python

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


```



#### [ queue_test.go ]( queue_test.go )

```golang

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


```



