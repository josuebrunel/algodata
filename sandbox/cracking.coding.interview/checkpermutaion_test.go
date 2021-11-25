package checkpermutation

import (
	"testing"
)

var cases = []struct {
	s1  string
	s2  string
	exp bool
}{
	{"God", "dog", false},
	{"god", "dog", true},
	{"god ", "dog", false},
	{"ello", "hello", false},
	{"cat", "dog", false},
	{"post", "poss", false},
}

func checkPermutation(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	cc := make([]int, 128)
	for _, c := range s1 {
		cc[c]++
	}
	for _, c := range s2 {
		cc[c]--
		if cc[c] < 0 {
			return false
		}
	}
	return true
}

func TestCheckPermutaion(t *testing.T) {
	for _, c := range cases {
		res := checkPermutation(c.s1, c.s2)
		t.Logf("<%s> is a permutation of <%s> ? (%v)", c.s1, c.s2, res)
		if res != c.exp {
			t.Errorf("Expected %v", c.exp)
		}
	}
}
