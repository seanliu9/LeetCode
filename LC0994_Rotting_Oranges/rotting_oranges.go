package main

import (
	"container/list"
	"math"
)

func orangesRotting(grid [][]int) int {
	m := len(grid)    // number of rows
	n := len(grid[0]) // number of columns
	total_oranges := 0
	num_rotten_oranges := 0

	// Keep track of rotten and non-rotten oranges.
	queue := list.New()
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != 0 {
				total_oranges += 1
			}
			if grid[i][j] == 2 {
				num_rotten_oranges += 1
				queue.PushBack([]int{i, j, 0})
			}
		}
	}

	// Perform BFS to simulate the oranges rotting.
	answer := 0
	for queue.Front() != nil {
		x := queue.Front()
		queue.Remove(x)
		vals := x.Value.([]int)
		curr_i, curr_j, curr_time := vals[0], vals[1], vals[2]
		answer = int(math.Max(float64(answer), float64(curr_time)))

		// Explore left neighbor (if it contains a non-rotten orange)
		if curr_j-1 >= 0 && grid[curr_i][curr_j-1] == 1 {
			num_rotten_oranges += 1
			grid[curr_i][curr_j-1] = 2
			queue.PushBack([]int{curr_i, curr_j - 1, curr_time + 1})
		}
		// Explore top neighbor (if it contains a non-rotten orange)
		if curr_i-1 >= 0 && grid[curr_i-1][curr_j] == 1 {
			num_rotten_oranges += 1
			grid[curr_i-1][curr_j] = 2
			queue.PushBack([]int{curr_i - 1, curr_j, curr_time + 1})
		}
		// Explore right neighbor (if it contains a non-rotten orange)
		if curr_j+1 < n && grid[curr_i][curr_j+1] == 1 {
			num_rotten_oranges += 1
			grid[curr_i][curr_j+1] = 2
			queue.PushBack([]int{curr_i, curr_j + 1, curr_time + 1})
		}
		// Explore bottom neighbor (if it contains a non-rotten orange)
		if curr_i+1 < m && grid[curr_i+1][curr_j] == 1 {
			num_rotten_oranges += 1
			grid[curr_i+1][curr_j] = 2
			queue.PushBack([]int{curr_i + 1, curr_j, curr_time + 1})
		}
	}

	if num_rotten_oranges == total_oranges {
		return answer
	} else { // if not oranges can rot
		return -1
	}
}
