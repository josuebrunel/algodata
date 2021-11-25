package isunique

import (
	"log"
	"testing"
)

var cases = []struct {
	Input  string
	Output bool
}{
	{"abcd", true},
	{"toto", false},
	{"joshua", true},
	{"", false},
	{"a", true},
}

func isUnique(s string) bool {
	if len(s) == 0 {
		return false
	}
	m := map[rune]int{}
	for _, c := range s {
		if _, ok := m[c]; ok {
			return false
		}
		m[c] = 1
	}
	return true
}

// TestIsUnique run tests againt isUnique func
func TestIsUnique(t *testing.T) {
	for _, c := range cases {
		output := isUnique(c.Input)
		log.Printf("Is %s made of unique characters ? : %v", c.Input, output)
		if output != c.Output {
			t.Errorf("Expected %v\n", c.Output)
		}
	}
}
