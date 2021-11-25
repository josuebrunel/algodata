package palindromepermu

import (
	"testing"
)

var cases = []struct {
	s string
	r bool
}{
	{"Tact Coa", true},
	{"Tact Coab", false},
	{"aab", true},
}

func getCharOrd(r rune) rune {
	if r < 'a' {
		return r + 32
	}
	return r
}

func isPalindromPerm(s string) bool {
	m := map[rune]int{}
	for _, c := range s {
		if (65 <= c && c <= 90) || (97 <= c && c <= 122) {
			m[getCharOrd(c)]++
		}
	}
	found := false
	for _, e := range m {
		if e%2 == 1 {
			if found {
				return false
			}
			found = true
		}
	}
	return true
}

func TestIsPalindromPermu(t *testing.T) {
	for _, c := range cases {
		r := isPalindromPerm(c.s)
		if r != c.r {
			t.Errorf("Expected %v", r)
		}
	}
}
