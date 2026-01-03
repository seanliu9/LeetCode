package main

import (
	"math"
)

func maxProduct(nums []int) int {
	n := len(nums)
	// trivial case
	if n == 1 {
		return nums[0]
	}

	maxProd, minProd, result := nums[0], nums[0], nums[0]

	for i := 1; i < n; i++ {
		if nums[i] < 0 {
			maxProd, minProd = minProd, maxProd
		}
		maxProd = int(math.Max(float64(nums[i]), float64(maxProd*nums[i])))
		minProd = int(math.Min(float64(nums[i]), float64(minProd*nums[i])))
		result = int(math.Max(float64(result), float64(maxProd)))
	}

	return result
}
