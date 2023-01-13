package main

import (
	"fmt"
	"reflect"
	"testing"
)

type Node struct {
	key  int
	val  int
	prev *Node
	next *Node
}

func (n Node) String() string {
	return fmt.Sprintf("(%v:%v) -> %v", n.key, n.val, n.next)
}

func NewNode(key, val int, prev, next *Node) *Node {
	return &Node{
		key:  key,
		val:  val,
		prev: prev,
		next: next,
	}
}

type LRUCache struct {
	capacity int
	cache    map[int]*Node
	head     *Node
	tail     *Node
}

func NewLRUCache(capacity int) *LRUCache {
	head := NewNode(0, 0, nil, nil)
	tail := NewNode(0, 0, head, nil)
	head.next = tail

	return &LRUCache{
		capacity: capacity,
		cache:    make(map[int]*Node),
		head:     head,
		tail:     tail,
	}
}

func (this *LRUCache) insert(node *Node) {
	prev, next := this.head, this.head.next
	prev.next, next.prev = node, node
	node.prev, node.next = prev, next
}

func (this *LRUCache) remove(node *Node) {
	prev, next := node.prev, node.next
	prev.next, next.prev = next, prev
}

func (this *LRUCache) Get(key int) int {
	node, ok := this.cache[key]
	if ok {
		this.remove(node)
		this.insert(node)
		return node.val
	}

	return -1
}

func (this *LRUCache) Put(key, val int) {
	node, ok := this.cache[key]
	if ok {
		this.remove(node)
	}

	node = NewNode(key, val, nil, nil)
	this.cache[key] = node
	this.insert(node)

	if len(this.cache) > this.capacity {
		lru := this.tail.prev
		this.remove(lru)
		delete(this.cache, lru.key)
	}
}

func TestLRUCache(t *testing.T) {
	cache := NewLRUCache(2)
	cache.Put(1, 1)
	cache.Put(2, 2)
	t.Log(cache.head)
	assert(t, cache.Get(1), 1)
	cache.Put(3, 3)
	t.Log(cache.head)
	assert(t, cache.Get(2), -1)
	cache.Put(4, 4)
	assert(t, cache.Get(3), 3)
	assert(t, cache.Get(4), 4)
	t.Log(cache.head)
}

func assert(t *testing.T, left, right any) {
	if !reflect.DeepEqual(left, right) {
		t.Errorf("%+v != %+v\n", left, right)
	}
}
