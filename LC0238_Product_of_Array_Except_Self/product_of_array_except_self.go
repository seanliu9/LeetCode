package main

func productExceptSelf(nums []int) []int {
	n := len(nums)
	result := make([]int, n)
	forward := make([]int, n)
	backward := make([]int, n)
	forward[0] = 1
	backward[n-1] = 1

	// Populate forward
	for i := 1; i < n; i++ {
		forward[i] = forward[i-1] * nums[i-1]
	}

	// Populate backward
	for i := n - 2; i >= 0; i-- {
		backward[i] = backward[i+1] * nums[i+1]
	}

	// Compute result
	for i := 0; i < n; i++ {
		result[i] = forward[i] * backward[i]
	}

	return result
}
