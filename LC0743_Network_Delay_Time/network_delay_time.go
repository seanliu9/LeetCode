package main

import (
	"container/heap"
	"math"
)

const INF = math.MaxInt32

type Pair struct {
	Key   int // used for ordering (min heap)
	Value int
}

type MinHeap []Pair

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i].Key < h[j].Key }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	*h = append(*h, x.(Pair))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

func networkDelayTime(times [][]int, n int, k int) int {
	adj := make(map[int][][2]int)
	visited := make(map[int]bool)
	min_times := make(map[int]int)
	for i := 1; i <= n; i++ {
		adj[i] = make([][2]int, 0)
		visited[i] = false
		min_times[i] = INF
	}

	// Construct graph, with cost of an edge as time it takes for a signal to travel that edge.
	for _, time := range times {
		u, v, w := time[0], time[1], time[2]
		adj[u] = append(adj[u], [2]int{v, w})
	}

	// Perform Dijkstra's from k
	pq := &MinHeap{}
	heap.Init(pq)

	heap.Push(pq, Pair{Key: 0, Value: k})

	for pq.Len() > 0 {
		x := heap.Pop(pq).(Pair)
		curr_time, curr_node := x.Key, x.Value

		if !visited[curr_node] {
			visited[curr_node] = true
			min_times[curr_node] = curr_time
			// Enqueue all the unvisited neighbors of curr_node.
			for _, edge := range adj[curr_node] {
				target, cost := edge[0], edge[1]
				if !visited[target] {
					heap.Push(pq, Pair{Key: curr_time + cost, Value: target})
				}
			}
		}
	}

	// Scan through min_times to find the longest times it takes any one node to receive the signal.
	answer := -1
	for _, time := range min_times {
		if time == INF {
			return -1
		}
		if time > answer {
			answer = time
		}
	}

	return answer
}
