package main

import (
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rHeight(root *TreeNode, max_path_length *int) int {
	if root == nil {
		return 0
	}
	left_subtree_height := rHeight(root.Left, max_path_length)
	right_subtree_height := rHeight(root.Right, max_path_length)
	*max_path_length = int(math.Max(float64(*max_path_length), float64(left_subtree_height+right_subtree_height)))
	return 1 + int(math.Max(float64(left_subtree_height), float64(right_subtree_height)))
}

func diameterOfBinaryTree(root *TreeNode) int {
	max_path_length := 0
	rHeight(root, &max_path_length)
	return max_path_length
}
