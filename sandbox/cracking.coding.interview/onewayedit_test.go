package onewayedit

import (
	"testing"
)

var cases = []struct {
	s1  string
	s2  string
	res bool
}{
	{"pale", "ple", true},
	{"pales", "pale", true},
	{"pale", "bale", true},
	{"pale", "bake", false},
}

func abs(i int) int {
	if i < 0 {
		return i * -1
	}
	return i
}

func oneWayEdit(s1, s2 string) bool {
	l := len(s1) - len(s2)
	if abs(l) > 1 {
		return false
	}
	ss := make([]int, 128)
	for _, c := range s1 {
		ss[c]++
	}
	for _, c := range s2 {
		ss[c]--
	}
	f := false
	for _, v := range ss {
		if v == -1 {
			if f == true {
				return false
			}
			f = true
		}
	}
	return true
}

func TestOneWayEdit(t *testing.T) {
	for _, c := range cases {
		r := oneWayEdit(c.s1, c.s2)
		t.Logf("<%s> is one edit away from <%s> => %t\n", c.s1, c.s2, r)
		if r != c.res {
			t.Errorf("Expected %v", r)
		}
	}
}
