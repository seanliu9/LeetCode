from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # For each bar, find the tallest bar to its left (can be itself)
        tallest_left = -1
        tallest_bar_left = [0] * n
        for i in range(n):
            tallest_left = max(tallest_left, height[i])
            tallest_bar_left[i] = tallest_left
        
        # Similarly, for each bar, find the tallest bar to its right (can be itself)
        tallest_right = -1
        tallest_bar_right = [0] * n
        for i in range(n - 1, -1, -1):
            tallest_right = max(tallest_right, height[i])
            tallest_bar_right[i] = tallest_right
        
        # For each bar, use its tallest bar to both sides to compute how much water it traps
        # amount of water on bar = min(tallest to left, tallest to right) - bar's height
        running_total = 0
        for i in range(n):
            running_total += min(tallest_bar_left[i], tallest_bar_right[i]) - height[i]

        return running_total