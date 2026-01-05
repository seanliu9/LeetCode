package main

func wordBreak(s string, wordDict []string) bool {
	wordDict_set := make(map[string]bool)
	n := len(s)
	// dp[i] = if we can properly segment the substring s[i...n - 1]
	dp := make([]bool, n+1)
	dp[n] = true
	max_word_length := -1
	for _, word := range wordDict {
		wordDict_set[word] = true
		x := len(word)
		if x > max_word_length {
			max_word_length = x
		}
	}
	for i := n - 1; i >= 0; i-- {
		for j := i; j < i+max_word_length && j < n; j++ {
			_, exists := wordDict_set[s[i:j+1]]
			if dp[j+1] && exists {
				dp[i] = true
				break // Exit j loop
			}
		}
	}

	return dp[0]
}
