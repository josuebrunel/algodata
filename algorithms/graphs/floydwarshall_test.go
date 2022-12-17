package main

import (
	"math"
	"reflect"
	"testing"
)

type T [][]int

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func floydwarshall(N int, edges T) T {
	distances := make([][]int, N)
	for i := range distances {
		distances[i] = make([]int, N)
	}
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if i == j {
				continue
			}
			distances[i][j] = math.MaxInt32
		}
	}
	for _, e := range edges {
		u := e[0]
		v := e[1]
		w := e[2]
		distances[u-1][v-1] = w
	}
	for k := 0; k < N; k++ {
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				distances[i][j] = min(distances[i][j], distances[i][k]+distances[k][j])
			}
		}
	}
	return distances
}

func TestFloydWarshal(t *testing.T) {
	edges := T{{1, 3, -2}, {3, 4, 2}, {4, 2, -1}, {2, 3, 3}, {2, 1, 4}}
	expected := T{{0, -1, -2, 0}, {4, 0, 2, 4}, {5, 1, 0, 2}, {3, -1, 1, 0}}
	result := floydwarshall(4, edges)
	if !reflect.DeepEqual(expected, result) {
		t.Fatalf("%v != %v", result, expected)
	}
	edges = T{{1, 2, 3}, {2, 1, 8}, {2, 3, 2}, {3, 1, 5}, {3, 4, 1},
		{4, 1, 2}, {1, 4, 7}}
	expected = T{{0, 3, 5, 6}, {5, 0, 2, 3}, {3, 6, 0, 1}, {2, 5, 7, 0}}
	result = floydwarshall(4, edges)
	if !reflect.DeepEqual(result, expected) {
		t.Fatalf("%v != %v", result, expected)
	}

}
