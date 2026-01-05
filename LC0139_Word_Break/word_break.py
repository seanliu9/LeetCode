from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)
        n = len(s)
        # dp[i] = if we can segment s[i...n - 1] into a combination of wordDict's words
        dp = [False] * (n + 1)
        dp[n] = True
        max_word_length = max(len(word) for word in wordDict)

        for i in range(n - 1, -1, -1):
            for j in range(i, min(i + max_word_length, n)):
                # dp[j + 1] represents if we can properly segment everything in s after index j
                # If so, then we check if the substring from i to j (both inclusive) can be properly segmented
                if dp[j + 1] and s[i: j + 1] in wordDict_set:
                    dp[i] = True
                    break # Exit j loop

        return dp[0]