package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rLCA(root, p, q *TreeNode) *TreeNode {
	if root == nil || root == p || root == q {
		return root
	}
	left := rLCA(root.Left, p, q)
	right := rLCA(root.Right, p, q)
	if left != nil && right != nil {
		return root
	}

	if left != nil {
		return left
	}
	return right
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	return rLCA(root, p, q)
}
