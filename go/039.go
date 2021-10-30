package main

import (
	"math"
	"./common"
)

func max(v []int) (m int) {
	for i, e := range v {
		if i == 0 || e > m {
			m = e
		}
	}
	return;
}

func index(v []int, m int) (n int) {
	n = -1
	for i, e := range v {
		if e == m {
			n = i
			break;
		}
	}
	return;
}

func main() {
	solutions := make([]int, 1001)

	for a := 1; a <= 1000; a++ {
		a2 := a * a;
		for b := 1; b <= 1000; b++ {
			c2 := a2 + b * b;
			c := int(math.Sqrt(float64(c2)))

			if c*c != c2{
				continue;
			}

			p := a + b + c
			if p > 1000 {
				continue;
			}

			solutions[p]++
		}
	}

	result := index(solutions, max(solutions))
	common.CheckInt(result, 39, "fa83a11a198d5a7f0bf77a1987bcd006")
}
