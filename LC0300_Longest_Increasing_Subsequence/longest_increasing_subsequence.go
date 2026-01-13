package main

import (
	"math"
)

func lengthOfLIS(nums []int) int {
	n := len(nums)
	if n == 1 {
		return 1
	}

	dp_A := make([]int, n) // dp_A[i] = length of longest increasing subsequence up to i if we do NOT include nums[i]
	dp_B := make([]int, n) // dp_B[i] = length of longest increasing subsequence up to i if we include nums[i]
	dp_A[0] = 0
	dp_B[0] = 1
	for i := 1; i < n; i++ {
		dp_A[i] = int(math.Max(float64(dp_A[i-1]), float64(dp_B[i-1])))
		// Out of all the values from nums[0] to nums[i - 1], find the optimal predecessor of nums[i]
		temp := math.Inf(-1)
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] {
				temp = math.Max(float64(dp_B[j]+1), temp)
			}
			dp_B[i] = int(math.Max(temp, 1.0))
		}
	}
	return int(math.Max(float64(dp_A[n-1]), float64(dp_B[n-1])))
}
