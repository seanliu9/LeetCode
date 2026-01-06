from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # trivial cases
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        max_length = 1
        nums = list(set(nums)) # Delete repeated numbers
        ranges = {num: [num, num] for num in nums} # maps number to the min and max of its longest consecutive elements sequence
        #print(ranges)
        for num in nums:
            # Check 1 below
            if num - 1 in ranges:
                ranges[num][0] = min(ranges[num][0], ranges[num - 1][0])
                ranges[ranges[num - 1][0]] = ranges[num]

            # Check 1 above
            if num + 1 in ranges:
                ranges[num][1] = max(ranges[num][1], ranges[num + 1][1])
                ranges[ranges[num + 1][1]] = ranges[num]

            max_length = max(max_length, ranges[num][1] - ranges[num][0] + 1)
        #print(ranges)
        return max_length