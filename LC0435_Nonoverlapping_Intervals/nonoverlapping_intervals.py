from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0

        # Sort the intervals by non-decreasing order of end.
        intervals = sorted(intervals, key = lambda x: x[1])
        dp = [0] * n # dp[i] = number of intervals we must remove to take the intervals up to the i-th non-overlapping
        most_recent_end = intervals[0][1]
        for i in range(1, n):
            curr_interval = intervals[i]
            if curr_interval[0] < most_recent_end: # if curr_interval overlaps with the previous one
                dp[i] = dp[i - 1] + 1
            else: # no need to remove curr_interval
                dp[i] = dp[i - 1]
                most_recent_end = curr_interval[1]

        return dp[n - 1]



        