package main

import "math"

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
