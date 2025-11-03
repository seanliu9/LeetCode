from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        # Split the elements in nums into a positive, negative, and zero lists.
        positives = []
        negatives = []
        zeros = []
        for x in nums:
            if x > 0:
                positives.append(x)
            elif x < 0:
                negatives.append(x)
            else:
                zeros.append(x)

        # Convert positives and negatives into a set (for O(1) lookup time)
        positives_set = set(positives)
        negatives_set = set(negatives)

        # Check if there is at least 3 0's in zeros
        if len(zeros) >= 3:
            result.add(tuple(sorted([0, 0, 0])))
        
        # If there is at least one 0, we find a positive integer x such that both x and -x exist
        if len(zeros) >= 1:
            for positive_num in positives:
                if -positive_num in negatives_set:
                    result.add(tuple(sorted([-positive_num, 0, positive_num])))

        # For each pair of 2 positive numbers, check if the negate of their sum exists.
        if len(positives) >= 2:
            for i in range(len(positives) - 1):
                for j in range(i + 1, len(positives), 1):
                    target = -(positives[i] + positives[j])
                    if target in negatives_set:
                        result.add(tuple(sorted([target, positives[i], positives[j]])))
        
        # Similarly, for each pair of 2 negative numbers, check if the negate of their sum exists.
        if len(negatives) >= 2:
            for i in range(len(negatives) - 1):
                for j in range(i + 1, len(negatives), 1):
                    target = -(negatives[i] + negatives[j])
                    if -(negatives[i] + negatives[j]) in positives_set:
                        result.add(tuple(sorted([negatives[i], negatives[j], target])))

        return list(result)