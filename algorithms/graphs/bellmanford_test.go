package main

import (
	"math"
	"reflect"
	"testing"
)

// type V interface {
// 	string | int32
// }

type EG struct {
	u string
	v string
	w int
}

type E []EG

func deepCopy(m map[string]int) map[string]int {
	var mcopy = make(map[string]int)
	for k, v := range m {
		mcopy[k] = v
	}
	return mcopy
}

func bellmanFord(N int, src string, edges E) map[string]int {
	dist := map[string]int{}
	for _, e := range edges {
		dist[e.u] = math.MaxInt32
		dist[e.v] = math.MaxInt32
	}
	dist[src] = 0

	for i := 0; i < N; i++ {
		distCopy := deepCopy(dist)
		for _, e := range edges {
			if dist[e.u] == math.MaxInt32 {
				continue
			}
			if dist[e.u]+e.w < distCopy[e.v] {
				distCopy[e.v] = distCopy[e.u] + e.w
			}
		}
		dist = distCopy
	}

	return dist
}

func TestBellmanFord(t *testing.T) {
	edges := E{{"S", "A", 10}, {"S", "E", 8}, {"E", "D", 1}, {"D", "A", -4},
		{"D", "C", -1}, {"A", "C", 2}, {"C", "B", -2}, {"B", "A", 1}}
	res := bellmanFord(6, "S", edges)
	expected := map[string]int{"S": 0, "A": 5, "E": 8, "D": 9, "C": 7, "B": 5}
	if !reflect.DeepEqual(res, expected) {
		t.Fatalf("%v != %v", res, expected)
	}

}
