package main

import (
	"container/list"
)

func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	if n == 1 {
		return []int{0}
	}
	answer := make([]int, n)
	stack := list.New() // stack is a decreasing stack
	stack.PushBack([]int{temperatures[n-1], n - 1})
	for i := n - 2; i >= 0; i-- {
		// Keep popping from stack until we see a temperature higher than temperatures[i]
		for stack.Len() > 0 && stack.Back().Value.([]int)[0] <= temperatures[i] {
			top := stack.Back()
			stack.Remove(top)
		}
		if stack.Len() == 0 {
			// if there is no day that is hotter than day i
			answer[i] = 0
		} else {
			answer[i] = stack.Back().Value.([]int)[1] - i
		}
		stack.PushBack([]int{temperatures[i], i})
	}
	return answer
}
