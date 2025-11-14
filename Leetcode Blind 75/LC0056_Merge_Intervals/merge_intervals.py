from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        # edge case
        if n == 1:
            return intervals
        
        # Sort intervals by the first element of each interval
        # If first element is tied, then sort by the second element of each interval
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        # Now the intervals are sorted by increasing order of start
        i = 0
        result = []
        while i < n:
            merged_interval_start = sorted_intervals[i][0]
            merged_interval_end = sorted_intervals[i][1]
            # Keep comparing every 2 adjacent intervals to check if they overlap
            while i < n - 1 and merged_interval_end >= sorted_intervals[i + 1][0]:
                # Merge two intervals if they overlap
                merged_interval_start = min(merged_interval_start, sorted_intervals[i + 1][0])
                merged_interval_end = max(merged_interval_end, sorted_intervals[i + 1][1])
                i += 1
            result.append([merged_interval_start, merged_interval_end])
            i += 1

        return result
            