package main

import "math"

// basic solution
func maxSubArray(nums []int) int {
	max_sum := int(math.Inf(-1))
	curr_sum := 0
	for i := range nums {
		curr_sum += nums[i]
		if curr_sum > max_sum {
			max_sum = curr_sum
		}
		if curr_sum < 0 {
			curr_sum = 0
		}
	}

	return max_sum
}

// DP solution
func maxSubArray_DP(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}

	dp_A := make([]int, n) // dp_A[i] = max subarray sum when we MUST include nums[i]
	dp_B := make([]int, n) // dp_B[i] = max subarray sum when we CANNOT include nums[i]

	dp_A[0] = nums[0]
	dp_B[0] = nums[0]

	for i := 1; i < n; i++ {
		dp_A[i] = int(math.Max(float64(dp_A[i-1]+nums[i]), float64(nums[i])))
		dp_B[i] = int(math.Max(float64(dp_A[i-1]), float64(dp_B[i-1])))
	}

	return int(math.Max(float64(dp_A[n-1]), float64(dp_B[n-1])))
}
