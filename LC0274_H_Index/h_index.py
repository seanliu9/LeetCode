from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # trivial cases
        if n == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        citations = sorted(citations)
        # For a paper with x citations, check if there are at least x papers, each of which has at least x citations.
        h_index = 0
        temp = 0
        for i in range(n):
            if citations[i] == 0:
                temp = 0
            else:
                temp = min(citations[i], n - i)
            h_index = max(h_index, temp)
        return h_index