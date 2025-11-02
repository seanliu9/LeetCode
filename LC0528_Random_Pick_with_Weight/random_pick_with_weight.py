import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        # e.g. if w = [1, 3, 4, 2], then weights = [0.1, 0.4, 0.8, 1]
        total = sum(self.w)
        self.weights = [x / total for x in self.w]
        for i in range(1, len(self.weights), 1):
            self.weights[i] += self.weights[i - 1]
    
    def pickIndex(self) -> int:
        rand = random.random()
        # Use self.weights to determine which index to pick
        for i in range(len(self.weights)):
            if rand < self.weights[i]:
                return i