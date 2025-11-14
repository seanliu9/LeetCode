from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        # edge case
        if len(intervals) == 0:
            return [newInterval]
        elif newInterval[0] > intervals[n - 1][1]:
            # if newInterval is larger than all the intervals
            intervals.append(newInterval)
            return intervals
        elif newInterval[1] < intervals[0][0]:
            # if newInterval is smaller than all the intervals
            return [newInterval] + intervals

        result = []
        # Copy from intervals to result until we find where to start merging
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Now we see where to start merging, so we perform the merge
        merged_interval_start = min(intervals[i][0], newInterval[0])
        while i < n and newInterval[1] >= intervals[i][0]:
            i += 1

        merged_interval_end = max(intervals[i - 1][1], newInterval[1])
        result.append([merged_interval_start, merged_interval_end])

        # Finish copying from intervals to result
        while i < n:
            result.append(intervals[i])
            i += 1

        return result