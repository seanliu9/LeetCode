package main

// Both start and end indices are inclusive.
func rBinarySearch(nums []int, target int, start int, end int) int {
	for start <= end {
		mid := (start + end) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			// Recurse on the right half
			return rBinarySearch(nums, target, mid+1, end)
		} else {
			// Recurse on the left half
			return rBinarySearch(nums, target, start, mid-1)
		}
	}
	// At this point we still can't find target, but we know where to insert it.
	return start
}

func searchInsert(nums []int, target int) int {
	n := len(nums)
	// trivial cases
	if target < nums[0] {
		return 0
	}
	if target > nums[n-1] {
		return n
	}
	return rBinarySearch(nums, target, 0, n-1)
}
