from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        # Sort points by increasing order of start
        points = sorted(points, key = lambda x: x[0])
        left = points[0][0] # the furthest left we can shoot an arrow and maximize the number of balloons popped by it
        right = points[0][1] # the furthest right we can shoot an arrow and maximize the number of balloons popped by it
        dp = [1] * n # dp[i] = minimum number of arrows needed to burst the balloons up to the i-th
        for i in range(1, n):
            if points[i][0] <= right:
                # if the current arrow can burst the i-th balloon
                dp[i] = dp[i - 1]
                # Update the boundaries
                left = points[i][0]
                right = min(right, points[i][1])
            else:
                # if the current arrow cannot burst the i-th balloon
                dp[i] = dp[i - 1] + 1
                # Reset the boundaries
                left = points[i][0]
                right = points[i][1]
        return dp[n - 1]
