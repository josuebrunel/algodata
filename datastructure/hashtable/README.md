* [hashtable.py](#-hashtablepy-)
* [hashtable_test.go](#-hashtable_testgo-)
#### [ hashtable.py ]( hashtable.py )

```python

import unittest


class Node:
    def __init__(self, key, val=None, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f"{self.key} -> {self.next}"


class Bucket:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f"({self.head})"

    def insert(self, key, val=None):
        if self.search(key):
            return
        node = Node(key, val, nxt=self.head)
        self.head = node

    def search(self, key):
        if not self.head:
            return
        cnode = self.head
        while cnode:
            if cnode.key == key:
                break
            cnode = cnode.next
        if not cnode:
            return
        return cnode.val

    def delete(self, key):
        if not self.head:
            return
        if self.head.key == key:
            self.head = self.head.next
            return
        cnode = self.head
        prev = None
        while cnode:
            if cnode.key == key:
                break
            prev = cnode
            cnode = cnode.next
        prev.next = cnode.next


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.array = []
        for _ in range(self.size):
            self.array.append(Bucket())

    def __repr__(self):
        return f"{self.array}"

    def xhash(self, key):
        return sum([ord(c) for c in str(key)]) % self.size

    def put(self, key, val):
        index = self.xhash(key)
        self.array[index].insert(key, val)

    def get(self, key):
        index = self.xhash(key)
        return self.array[index].search(key)

    def remove(self, key):
        index = self.xhash(key)
        return self.array[index].delete(key)


class TestHashTable(unittest.TestCase):
    def test_hasttable(self):
        h = HashTable(10)
        h.put("josh", {"age": 32})
        h.put("josh", "someone")
        h.put(10, "dix")
        h.put("cat", "pet")
        h.put("tac", "sweet")
        print(h)
        self.assertEqual(h.get("josh"), {"age": 32})
        self.assertEqual(h.get(10), "dix")
        self.assertEqual(h.get("cat"), "pet")
        h.remove("cat")
        print(h)
        self.assertEqual(h.get("cat"), None)
        self.assertEqual(h.get("tac"), "sweet")


if __name__ == "__main__":
    unittest.main()


```



#### [ hashtable_test.go ]( hashtable_test.go )

```golang

package hashtable

import (
	"fmt"
	"testing"
)

// Node represents a node in a bucket
type Node struct {
	key  string
	val  interface{}
	next *Node
}

func (n Node) String() string {
	if n.next == nil {
		return fmt.Sprintf("%s -> nil", n.key)
	}
	return fmt.Sprintf("%s -> %s", n.key, n.next)
}

// Bucket represents a sequence of connected nodes
type Bucket struct {
	head *Node
}

func (b Bucket) String() string {
	return fmt.Sprintf("(%s)", b.head)
}

func (b *Bucket) insert(key string, val interface{}) {
	node := b.search(key)
	if node != nil {
		node.val = val
		return
	}
	node = &Node{key, val, b.head}
	b.head = node
}

func (b Bucket) search(key string) *Node {
	if b.head == nil {
		return nil
	}
	cnode := b.head
	for cnode != nil {
		if cnode.key == key {
			break
		}
		cnode = cnode.next
	}
	if cnode == nil {
		return nil
	}
	return cnode
}

func (b *Bucket) delete(key string) {
	if b.head == nil {
		return
	}
	if b.head.key == key {
		b.head = b.head.next
		return
	}
	cnode := b.head
	prev := &Node{}
	for cnode != nil {
		if cnode.key == key {
			break
		}
		prev = cnode
		cnode = cnode.next
	}
	prev.next = cnode.next
}

// HashTable represents an associated array
type HashTable struct {
	size  int
	array []*Bucket
}

func (h HashTable) String() string {
	return fmt.Sprintf("%s", h.array)
}

// New initiates a new HashTable
func New(size int) *HashTable {
	var array = make([]*Bucket, size)
	for i := range array {
		array[i] = &Bucket{}
	}
	return &HashTable{size, array}
}

func (h HashTable) hash(key string) int {
	var sum int
	for i := 0; i < len(key); i++ {
		sum += int(key[i])
	}
	return sum % h.size
}

func (h *HashTable) put(key string, val interface{}) {
	index := h.hash(key)
	h.array[index].insert(key, val)
	return
}

func (h HashTable) get(key string) interface{} {
	index := h.hash(key)
	node := h.array[index].search(key)
	if node == nil {
		return nil
	}
	return node.val
}

func (h *HashTable) remove(key string) {
	index := h.hash(key)
	h.array[index].delete(key)
	return
}

func TestHashTable(t *testing.T) {
	h := New(10)
	h.put("name", "josh")
	type Person struct {
		name string
		age  int
	}
	josh := Person{"josh", 32}
	h.put("josh", josh)
	h.put("cat", "pet")
	h.put("tac", "sweet")
	t.Logf("%s", h)
	value := h.get("name")
	if value != "josh" {
		t.Fatalf("Unexpected value returned (%v)", value)
	}
	value = h.get("josh")
	if value != josh {
		t.Fatalf("Unexpected value returned (%v)", value)
	}
	h.remove("cat")
	value = h.get("cat")
	t.Logf("%s", h)
	if value != nil {
		t.Fatalf("Unexpected value returned (%v)", value)
	}
	// update value
	h.put("tac", "tic")
	value = h.get("tac")
	if value != "tic" {
		t.Fatalf("Unexpected value returned (%v)", value)
	}
}


```



