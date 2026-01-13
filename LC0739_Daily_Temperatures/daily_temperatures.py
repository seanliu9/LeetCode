from collections import deque
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1:
            return [0]
        answer = [0] * n
        stack = deque() # stack is a decreasing stack
        stack.append((temperatures[n - 1], n - 1))
        for i in range(n - 2, -1, -1):
            # Keep popping from the stack until we see a temperature greater than temperatures[i]
            while len(stack) > 0 and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if len(stack) == 0:
                answer[i] = 0
            else:
                answer[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        
        return answer
           

