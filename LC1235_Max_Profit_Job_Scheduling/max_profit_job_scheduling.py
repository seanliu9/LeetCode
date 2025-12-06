from typing import List

class Solution:
    # Both left and right boundaries are inclusive.
    def rBinarySearch(self, arr: List[int], left: int, right: int, target: int, idx: int = -1) -> int:
        if left > right:
            return idx
        mid = (left + right) // 2
        if arr[mid] <= target:
            idx = mid
            return self.rBinarySearch(arr, mid + 1, right, target, idx)  
        else:
            return self.rBinarySearch(arr, left, mid - 1, target, idx)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        if n == 1:
            return profit[0]
        
        # Sort classes by increasing order of endTime
        combined = list(zip(startTime, endTime, profit))
        combined_sorted = sorted(combined, key = lambda x: x[1])
        startTimes, endTime_sorted, profits = zip(*combined_sorted)
        startTimes = list(startTimes)
        endTime_sorted = list(endTime_sorted)
        profits = list(profits)

        # For each job, compute the index of the last compatible job before it (i.e. ends before this job starts)
        last_compatible_job = [-1] * n
        for i in range(1, n):
            # Do a binary search on endTime_sorted for the latest-ending job that ends before job i starts.
            last_compatible_job[i] = self.rBinarySearch(endTime_sorted, 0, i - 1, startTimes[i])

        dp = [[-1] * 2 for _ in range(n)]
        # dp[i, 0] = max value we can get up to the i-th job if we don't do job i
        # dp[i, 1] = max value we can get up to the i-th job if we do job i

        # base cases
        dp[0][0] = 0
        dp[0][1] = profits[0]

        # recurrence
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            if last_compatible_job[i] == -1:
                # if no job is compatible with the i-th job, we can only do the i-th job (and nothing before it)
                dp[i][1] = profits[i]
            else:
                dp[i][1] = max(dp[last_compatible_job[i]][0], dp[last_compatible_job[i]][1]) + profits[i]
        
        return max(dp[n - 1][0], dp[n - 1][1])