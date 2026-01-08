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

// D&C solution
func rMaxSubArray(nums []int, start int, end int) [4]int {
	// base case
	if start == end {
		return [4]int{nums[start], nums[start], nums[start], nums[start]}
	}
	mid := (start + end) / 2
	left_answer := rMaxSubArray(nums, start, mid)
	left_total, left_start, left_end, left_overall := left_answer[0], left_answer[1], left_answer[2], left_answer[3]
	right_answer := rMaxSubArray(nums, mid+1, end)
	right_total, right_start, right_end, right_overall := right_answer[0], right_answer[1], right_answer[2], right_answer[3]

	// Merge left and right halves' solutions
	total := left_total + right_total
	start_max := int(math.Max(float64(left_start), float64(left_total+right_start)))
	end_max := int(math.Max(float64(right_end), float64(right_total+left_end)))
	overall_max := int(math.Max(math.Max(float64(left_overall), float64(right_overall)), float64(left_end+right_start)))
	return [4]int{total, start_max, end_max, overall_max}
}

func maxSubArray_DC(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	return rMaxSubArray(nums, 0, n-1)[3]

}
