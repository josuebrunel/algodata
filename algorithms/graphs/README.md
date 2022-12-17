* [bellmanford.py](#-bellmanfordpy-)
* [bellmanford_test.go](#-bellmanford_testgo-)
* [djikstra.py](#-djikstrapy-)
* [dsu.py](#-dsupy-)
* [dsu_test.go](#-dsu_testgo-)
* [floydwarshall.py](#-floydwarshallpy-)
* [floydwarshall_test.go](#-floydwarshall_testgo-)
#### [ bellmanford.py ]( bellmanford.py )

```python

import unittest


# O(v*E)
def bellman_ford(n, edges, src):
    """The idea is to compute the shortest
    for N-1 times. At each iteration:
    - if src weight is infinity, we skip
    - if src weight + dst weight < temporary dst weight
    we update temporary dst weight
    - after each iteration, temporary weights holder become
    original weights
    - to validate the result we should one more iteration
    and make sure that values haven't changes. If values
    changes after N iteration it means that we have a
    negative weight cycle
    """
    inf = float("inf")
    adj = {}
    for s, d, _ in edges:
        adj[s] = inf
        adj[d] = inf

    adj[src] = 0

    for _ in range(n):
        tmp = adj.copy()
        for s, d, w in edges:
            if adj[s] == inf:
                continue
            if adj[s] + w < tmp[d]:
                tmp[d] = tmp[s] + w
            print(adj, tmp)

        adj = tmp

    return adj.values()


class BellmanFordTest(unittest.TestCase):

    def test_bellman_ford(self):
        edges = [["S", "A", 10], ["S", "E", 8], ["E", "D", 1], ["D", "A", -4],
                 ["D", "C", -1], ["A", "C", 2], ["C", "B", -2], ["B", "A", 1]]
        self.assertCountEqual(bellman_ford(6, edges, "S"), [0, 5, 5, 7, 9, 8])


if __name__ == "__main__":
    unittest.main()


```



#### [ bellmanford_test.go ]( bellmanford_test.go )

```golang

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

func bellmanFord(N int, src string, edges E) map[string]int {
	dist := map[string]int{}
	for _, e := range edges {
		dist[e.u] = math.MaxInt32
		dist[e.v] = math.MaxInt32
	}
	dist[src] = 0

	for i := 0; i < N; i++ {
		distCopy := dist
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


```



#### [ djikstra.py ]( djikstra.py )

```python

import unittest
import collections
import heapq


def djikstra(edges):
    adj = collections.defaultdict(list)
    for src, dst, wgh in edges:
        adj[src].append((dst, wgh))
        adj[dst] = adj.get(dst, [])

    visited = set()
    heap = []
    heapq.heappush(heap, (0, 0))
    shortest = [float("inf")] * len(adj)

    while heap:
        weight, edge = heapq.heappop(heap)
        if edge in visited:
            continue

        visited.add(edge)
        for ne, nw in adj[edge]:
            if ne in visited:
                continue
            heapq.heappush(heap, (weight + nw, ne))

        shortest[edge] = weight

    return shortest


class DjikstraTest(unittest.TestCase):

    def test_djikstra(self):
        edges = [[0, 1, 2], [0, 2, 6], [2, 3, 8], [1, 3, 5], [3, 4, 10],
                 [3, 5, 15], [4, 5, 6], [4, 6, 2], [5, 6, 6]]
        shortest = [0, 2, 6, 7, 17, 22, 19]
        self.assertEqual(djikstra(edges), shortest)


if __name__ == "__main__":
    unittest.main()


```



#### [ dsu.py ]( dsu.py )

```python

import unittest


class DSU:

    def __init__(self, N):
        self.parents = {i: i for i in range(N)}
        self.ranks = {i: 0 for i in range(N)}

    def find(self, u):
        u = self.parents[u]
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
        return u

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        if self.ranks[u] > self.ranks[v]:
            self.parents[v] = u
        elif self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
        else:
            self.parents[u] = v
            self.ranks[v] += 1
        return True


class DSUTest(unittest.TestCase):

    def test_dsu(self):
        edges = [[1, 2], [4, 1], [2, 4], [2, 3]]
        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            dsu.union(u, v)
        self.assertEqual(dsu.union(4, 1), False)


if __name__ == "__main__":
    unittest.main()


```



#### [ dsu_test.go ]( dsu_test.go )

```golang

package main

import "testing"

type DSU struct {
	Parents map[int]int
	Ranks   map[int]int
}

func NewDSU(n int) DSU {
	dsu := DSU{map[int]int{}, map[int]int{}}
	for i := 0; i < n+1; i++ {
		dsu.Parents[i] = i
		dsu.Ranks[i] = 0
	}
	return dsu
}

func (d *DSU) Find(u int) int {
	u = d.Parents[u]
	for u != d.Parents[u] {
		d.Parents[u] = d.Parents[d.Parents[u]]
		u = d.Parents[u]
	}
	return u
}

func (d *DSU) Union(u, v int) bool {
	u, v = d.Find(u), d.Find(v)
	if u == v {
		return false
	}

	if d.Ranks[u] > d.Ranks[v] {
		d.Parents[v] = u
	} else if d.Ranks[u] < d.Ranks[v] {
		d.Parents[u] = v
	} else {
		d.Parents[u] = v
		d.Ranks[v]++
	}
	return true
}

func TestDSU(t *testing.T) {
	edges := [][2]int{{1, 2}, {4, 1}, {2, 4}, {2, 3}}
	dsu := NewDSU(len(edges))

	for _, e := range edges {
		u, v := e[0], e[1]
		dsu.Union(u, v)
	}

	if dsu.Union(4, 1) {
		t.Fatalf("False was expected for Union(4, 1)")
	}
}


```



#### [ floydwarshall.py ]( floydwarshall.py )

```python

import unittest


def floyd_warshall(n, edges):
    distances = [[float("inf")] * n for i in range(n)]
    for i in range(n):
        distances[i][i] = 0

    for u, v, w in edges:
        distances[u - 1][v - 1] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j],
                                      distances[i][k] + distances[k][j])
    return distances


class FloydWarshall(unittest.TestCase):

    def test_floyd_warshall(self):
        edges = [[1, 3, -2], [3, 4, 2], [4, 2, -1], [2, 3, 3], [2, 1, 4]]
        result = [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
        self.assertCountEqual(floyd_warshall(4, edges), result)
        edges = [[1, 2, 3], [2, 1, 8], [2, 3, 2], [3, 1, 5], [3, 4, 1],
                 [4, 1, 2], [1, 4, 7]]
        result = [[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]
        self.assertCountEqual(floyd_warshall(4, edges), result)


if __name__ == "__main__":
    unittest.main()


```



#### [ floydwarshall_test.go ]( floydwarshall_test.go )

```golang

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


```



