package main

import (
	"sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
	n := len(intervals)
	if n == 1 {
		return 0
	}

	// Sort intervals by non-decreasing order of end.
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	dp := make([]int, n) // dp[i] = number of intervals we must remove to make the intervals up to the i-th non-overlapping
	most_recent_end := intervals[0][1]
	curr_interval := intervals[0]
	for i := 1; i < n; i++ {
		curr_interval = intervals[i]
		if curr_interval[0] < most_recent_end { // if curr_interval overlaps with the previous one
			dp[i] = dp[i-1] + 1
		} else { // no overlap
			dp[i] = dp[i-1]
			most_recent_end = curr_interval[1]
		}
	}

	return dp[n-1]
}
