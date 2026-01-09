package main

func setZeroes(matrix [][]int) {
	m := len(matrix)    // number of rows
	n := len(matrix[0]) // number of columns

	// Determine if the topmost row and leftmost column have 0's.
	top_row_has_zero := false
	for j := 0; j < n; j++ {
		if matrix[0][j] == 0 {
			top_row_has_zero = true
			break
		}
	}

	leftmost_column_has_zero := false
	for i := 0; i < m; i++ {
		if matrix[i][0] == 0 {
			leftmost_column_has_zero = true
			break
		}
	}

	// Iterate through the matrix (excluding top row and leftmost column).
	// If we see a 0 at (i, j), then set matrix[i][0] and matrix[0][j] to 0.
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}

	// Using the top row and leftmost column as markers, set everything outside of them to 0 if necessary.
	// Check leftmost column
	for i := 1; i < m; i++ {
		if matrix[i][0] == 0 {
			for j := 1; j < n; j++ {
				matrix[i][j] = 0
			}
		}
	}
	// Check top row
	for j := 1; j < n; j++ {
		if matrix[0][j] == 0 {
			for i := 1; i < m; i++ {
				matrix[i][j] = 0
			}
		}
	}

	// Set top row and leftmost column to 0 if necessary.
	if top_row_has_zero {
		for j := 0; j < n; j++ {
			matrix[0][j] = 0
		}
	}
	if leftmost_column_has_zero {
		for i := 0; i < m; i++ {
			matrix[i][0] = 0
		}
	}
}
