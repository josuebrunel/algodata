package main

import (
	"log"
	"testing"
)

var cases = []struct {
	input  [][]int
	output [][]int
}{
	{
		[][]int{
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9},
		},
		[][]int{
			{7, 4, 1},
			{8, 5, 2},
			{9, 6, 3},
		},
	},
}

func rotateMatrix(m [][]int) [][]int {
	l := len(m)

	log.Printf("%v\n", m)
	for i := 0; i < l; i++ {
		for j := i; j < l; j++ {
			tmp := m[i][j]
			m[i][j] = m[j][i]
			m[j][i] = tmp
		}
	}
	log.Printf("Matrix transposed\n:%v\n", m)
	for i := 0; i < l; i++ {
		for j := 0; j < l/2; j++ {
			tmp := m[i][j]
			m[i][j] = m[i][l-1-j]
			m[i][l-1-j] = tmp
		}
	}
	log.Printf("Matrix rotated\n:%v\n", m)
	return m
}

func TestRotateMatrix(t *testing.T) {
	for _, c := range cases {
		r := rotateMatrix(c.input)
		if r != c.output {
			t.Errorf("Expected output: %v", c.output)
		}
	}
}
