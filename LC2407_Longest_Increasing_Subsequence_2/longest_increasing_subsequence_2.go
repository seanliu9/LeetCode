package main

import (
	"math"
)

func lengthOfLIS(nums []int, k int) int {
	n := len(nums)
	if n == 1 {
		return 1
	}
	dp_A := make([]int, n)
	dp_B := make([]int, n)
	dp_A[0] = 0
	dp_B[0] = 1
	lis := make(map[int]int)
	lis[nums[0]] = 1

	for i := 1; i < n; i++ {
		// Calculate dp_A[i]
		dp_A[i] = int(math.Max(float64(dp_A[i-1]), float64(dp_B[i-1])))

		// Calculate dp_B[i]
		// Consider all the values from nums[i] - k to nums[i] - 1 (both inclusive).
		x := math.Inf(-1)
		for j := k; j >= 1; j-- {
			val, exists := lis[nums[i]-j]
			if exists {
				x = math.Max(x, float64(val)+1.0)
			}
		}
		dp_B[i] = int(math.Max(1.0, x))
		lis[nums[i]] = dp_B[i]
	}

	return int(math.Max(float64(dp_A[n-1]), float64(dp_B[n-1])))
}
