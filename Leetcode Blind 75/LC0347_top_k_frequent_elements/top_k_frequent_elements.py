from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create dictionary mapping element in array to its frequency
        freq_dict = {}
        for x in nums:
            if x in freq_dict:
                freq_dict[x] += 1
            else:
                freq_dict[x] = 1
        
        # Sort freq_dict by decreasing order by values
        freq_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
        k_most_frequent = list(freq_dict.keys())[:k]
        return k_most_frequent