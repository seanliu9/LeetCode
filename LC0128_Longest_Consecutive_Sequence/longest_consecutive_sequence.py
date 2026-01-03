from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # trivial cases
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        nums_set = set(nums)
        max_length = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                length = 1

                while current + 1 in nums_set:
                    current += 1
                    length += 1

                max_length = max(max_length, length)
        
        return max_length