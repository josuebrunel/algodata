package main

import (
	"testing"
)

type Node struct {
	Children map[rune]*Node
	End      bool
}

func NewNode() *Node {
	children := make(map[rune]*Node)
	return &Node{Children: children}
}

type Trie struct {
	Root *Node
}

func NewTrie() *Trie {
	node := NewNode()
	return &Trie{node}
}

func (t *Trie) Add(word string) {
	cur := t.Root

	for _, c := range word {
		if _, ok := cur.Children[c]; !ok {
			cur.Children[c] = NewNode()
		}
		cur = cur.Children[c]
	}
	cur.End = true
}

func (t Trie) Search(word string) bool {
	cur := t.Root
	for _, c := range word {
		if _, ok := cur.Children[c]; !ok {
			return false
		}
		cur = cur.Children[c]
	}
	return cur.End
}

func (t Trie) Prefix(prefix string) bool {
	cur := t.Root
	for _, c := range prefix {
		if _, ok := cur.Children[c]; !ok {
			return false
		}
		cur = cur.Children[c]
	}
	return true
}

func TestHelloWorld(t *testing.T) {
	trie := NewTrie()
	trie.Add("daddy")
	trie.Add("hello")
	trie.Add("sad")
	trie.Add("bad")
	if !trie.Search("daddy") {
		t.Fatal("daddy not fond")
	}
	if !trie.Prefix("hel") {
		t.Fatal("hel prefix doesn't exist")
	}
	if trie.Search("hell") {
		t.Fatal("hell is not supposed to exist")
	}
}
