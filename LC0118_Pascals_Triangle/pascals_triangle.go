package main

func generate(numRows int) [][]int {
	// trivial cases
	if numRows == 1 {
		return [][]int{{1}}
	}
	if numRows == 2 {
		return [][]int{{1}, {1, 1}}
	}

	dp := make([][]int, numRows) // dp[i] = (i + 1)-th row of Pascal's triangle
	dp[0] = []int{1}
	dp[1] = []int{1, 1}
	for i := 2; i < numRows; i++ {
		dp[i] = make([]int, i+1)
		dp[i][0] = 1
		dp[i][i] = 1
		for j := 1; j < i; j++ {
			dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
		}
	}

	return dp
}
