package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rPathSum(root *TreeNode, targetSum int) int {
	// base case
	if root == nil {
		return 0
	}

	result := rPathSum(root.Left, targetSum-root.Val) + rPathSum(root.Right, targetSum-root.Val)
	if root.Val == targetSum {
		result += 1
	}
	return result
}

func pathSum(root *TreeNode, targetSum int) int {
	// trivial case
	if root == nil {
		return 0
	}

	// We must consider when the path contains root, and when the path does NOT contain root.
	return rPathSum(root, targetSum) + pathSum(root.Left, targetSum) + pathSum(root.Right, targetSum)
}
