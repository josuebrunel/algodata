* [djikstra.py](#-djikstrapy-)
* [dsu.py](#-dsupy-)
* [dsu_test.go](#-dsu_testgo-)
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



