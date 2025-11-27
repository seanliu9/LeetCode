from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # trivial cases
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        # Because houses 0 and n - 1 are adjacent in the circle, we can either consider
        # houses 0 to n - 2 or houses 1 to n - 1

        # T_1[i] is the max amount of money we can make from robbing houses 0 to i (inclusive)
        T_1 = [0] * (n - 1)
        T_1[0] = nums[0]
        T_1[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            # Either rob this house (but not the one immediately before it), or rob the house immediately before it (but not this house)
            T_1[i] = max(T_1[i - 2] + nums[i], T_1[i - 1])
        
        # T_2[i] is the max amount of money we can make from robbing houses 1 to i (inclusive)
        T_2 = [0] * n
        T_2[1] = nums[1]
        T_2[2] = max(nums[1], nums[2])
        for i in range(3, n):
            # Either rob this house (but not the one immediately before it), or rob the house immediately before it (but not this house)
            T_2[i] = max(T_2[i - 2] + nums[i], T_2[i - 1])
        
        return max(T_1[n - 2], T_2[n - 1])