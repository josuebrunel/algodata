* [stack.py](#-stackpy-)
* [stack_test.go](#-stack_testgo-)
#### [ stack.py ]( stack.py )

```python

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


```



#### [ stack_test.go ]( stack_test.go )

```golang

package main

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

// Stack represents a sequence of nodes
type Stack struct {
	head   *Node
	length int
}

// Push adds an element to the stack
func (s *Stack) Push(val int) {
	node := &Node{val, s.head}
	s.head = node
	s.length++
}

// Peek returns the element on top of the stack
func (s *Stack) Peek() int {
	return s.head.val
}

// Pop returns and remove the element on the top of the stack
func (s *Stack) Pop() int {
	if s.head == nil {
		return -1
	}
	val := s.head.val
	s.head = s.head.next
	s.length--
	return val
}

// MinMaxNode contains the min and max of a a stack when a new element is pushed in
type MinMaxNode struct {
	min, max int
	next     *MinMaxNode
}

// String is the string representation of a node
func (n MinMaxNode) String() string {
	if n.next == nil {
		return fmt.Sprintf("(%d, %d) -> nil", n.min, n.max)
	}
	return fmt.Sprintf("(%d, %d) -> %s", n.min, n.max, n.next)
}

// MinMax stack is a stack which tracks its min and the max values
type MinMaxStack struct {
	Stack
	minMax *MinMaxNode
}

func (m MinMaxStack) min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func (m MinMaxStack) max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func (m *MinMaxStack) Push(val int) {
	if m.Stack.head == nil {
		m.minMax = &MinMaxNode{val, val, nil}
	} else {
		newMin := m.min(val, m.minMax.min)
		newMax := m.max(val, m.minMax.max)
		m.minMax = &MinMaxNode{newMin, newMax, m.minMax}
	}
	m.Stack.Push(val)
}

func (m *MinMaxStack) Pop() int {
	if m.Stack.head == nil {
		return -1
	}
	val := m.Stack.Pop()
	m.minMax = m.minMax.next
	return val
}

// GetMin returns the minimum value in the stack
func (m MinMaxStack) GetMin() int {
	return m.minMax.min
}

// GetMax returns the maximum value in the stack
func (m MinMaxStack) GetMax() int {
	return m.minMax.max
}

func TestPush(t *testing.T) {
	s := Stack{&Node{1, nil}, 1}
	for i := 2; i <= 5; i++ {
		s.Push(i)
	}
	t.Logf("%s", s.head)
	if s.length != 5 {
		t.Fatalf("Unexpected length (%d)", s.length)
	}
	if s.head.val != 5 {
		t.Fatalf("Unexpected head value (%d)", s.head.val)
	}
}

func TestPeek(t *testing.T) {
	s := Stack{&Node{1, nil}, 1}
	for i := 2; i <= 5; i++ {
		s.Push(i)
	}
	t.Logf("%s", s.head)
	res := s.Peek()
	if res != 5 {
		t.Fatalf("Unexpected returned value (%d)", res)
	}
}

func TestPop(t *testing.T) {
	s := Stack{&Node{1, nil}, 1}
	for i := 2; i <= 5; i++ {
		s.Push(i)
	}
	t.Logf("%s", s.head)
	res := s.Pop()
	if res != 5 {
		t.Fatalf("Unexpected returned value (%d)", res)
	}
	s.Pop()
	t.Logf("%s", s.head)
	if s.length != 3 {
		t.Fatalf("Unexpected length (%d)", s.length)
	}
}

func TestMinMaxStack(t *testing.T) {
	s := MinMaxStack{}
	s.Push(1)
	s.Push(3)
	s.Push(-1)
	s.Push(6)
	t.Logf("Stack => %s\nMinMax => %s", s.head, s.minMax)
	if s.length != 4 {
		t.Fatalf("Unexpected length (%d)", s.length)
	}
	if s.head.val != 6 {
		t.Fatalf("Unexpected top of stack (%d)", s.head.val)
	}
	min, max := s.GetMin(), s.GetMax()
	if min != -1 {
		t.Fatalf("Unexpected min of stack (%d)", min)
	}
	if max != 6 {
		t.Fatalf("Unexpected max of stack (%d)", max)
	}
	s.Pop()
	s.Pop()
	min, max = s.GetMin(), s.GetMax()
	if min != 1 {
		t.Fatalf("Unexpected min of stack (%d)", min)
	}
	if max != 3 {
		t.Fatalf("Unexpected max of stack (%d)", max)
	}
	if s.length != 2 {
		t.Fatalf("Unexpected length (%d)", s.length)
	}
	t.Logf("Stack => %s\nMinMax => %s", s.head, s.minMax)
}


```



