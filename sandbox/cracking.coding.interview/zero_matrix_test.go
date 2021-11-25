package zeromatrix

import (
	"fmt"
	"testing"
)

func zeroMatrix(m [][]int) {
	l := len(m)
	for i := 0; i < l; i++ {
		ll := len(m[i])
		for j := 0; j < ll; j++ {
			if m[i][j] == 0 {
				fmt.Printf("0 found\nRow is %v\n", m[i])
				// set rows
				for x := 0; x < ll; x++ {
					if m[i][x] != 0 && m[i][x] != -1 {
						m[i][x] = -1
					}
				}
				// set columns
				for x := 0; x < l; x++ {
					if m[x][j] != 0 && m[x][j] != -1 {
						m[x][j] = -1
					}
				}
				m[i][j] = -1
				fmt.Printf("After: %v\n", m[i])
			}
		}
	}
	// loop over and set all -1 to 0
	for i := 0; i < l; i++ {
		ll := len(m[i])
		for j := 0; j < ll; j++ {
			if m[i][j] == -1 {
				m[i][j] = 0
			}
		}
	}
	fmt.Printf("Final: %v\n", m)
}

func TestZeroMatrix(t *testing.T) {
	zeroMatrix([][]int{
		[]int{0, 1, 2, 0},
		[]int{3, 4, 5, 2},
		[]int{1, 3, 1, 5},
	})
}
