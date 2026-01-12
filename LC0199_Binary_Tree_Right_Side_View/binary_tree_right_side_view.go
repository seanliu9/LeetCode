package main

import (
	"container/list"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	// trivial case
	if root == nil {
		return []int{}
	}

	// Perform level-order traversal on the tree, and the last node in the current level is the only visible node of the level.
	answer := make([]int, 0)
	queue := list.New()
	queue.PushBack(root)
	n := queue.Len()
	for n > 0 {
		answer = append(answer, queue.Back().Value.(*TreeNode).Val)
		for i := 0; i < n; i++ {
			head := queue.Front()
			curr_node := head.Value.(*TreeNode)
			queue.Remove(head)
			if curr_node.Left != nil {
				queue.PushBack(curr_node.Left)
			}
			if curr_node.Right != nil {
				queue.PushBack(curr_node.Right)
			}
		}
		n = queue.Len()
	}
	return answer
}
