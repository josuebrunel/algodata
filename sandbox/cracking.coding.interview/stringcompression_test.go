package stringcompression

import "testing"

var cases = []struct {
	input  string
	output string
}{
	{"aabcccccaaa", "a2blc5a3"},
	{"aaccNnZZ", "a2c2NnZ2"},
}

func stringCompression(s string) string {
	ct := 1
	ns := []rune{}
	l := len(s)
	for i := 0; i < l; i++ {
		if s[i+1] < l && s[i] == s[i+1] {
			ct++
		} else {
			if c != 0 {
				ns = append(ns)
			}
		}
	}
	return ns
}

func TestStringCompression(t *testing.T) {
	for _, c := range cases {
		r := stringCompression(c.input)
		t.Logf("<%s> compressed is : <%s>", c.input, r)
		if r != c.output {
			t.Errorf("Expected <%s>", c.output)
		}
	}
}
