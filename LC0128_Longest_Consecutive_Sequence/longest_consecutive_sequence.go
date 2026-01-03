package main

func longestConsecutive(nums []int) int {
	// trivial cases
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return 1
	}

	// Create dictionary from nums- we really only care about the key (to check if a number exists in nums).
	nums_set := make(map[int]int)
	for _, v := range nums {
		nums_set[v] = 0
	}
	max_length := 1
	for num, _ := range nums_set {
		_, exists := nums_set[num-1]
		length := 1
		if !exists { // if num is the start of a sequence
			current := num

			for {
				_, exists := nums_set[current+1]
				if !exists {
					break
				}
				length++
				current++
			}
			if length > max_length {
				max_length = length
			}
		}
	}

	return max_length
}
