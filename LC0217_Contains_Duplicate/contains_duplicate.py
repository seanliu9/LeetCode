# Problem: https://leetcode.com/problems/contains-duplicate/description/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for x in nums:
            if x in values:
                return True
            else:
                values.add(x)
        return False