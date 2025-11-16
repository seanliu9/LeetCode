def decompress(s: str) -> str:
	result = ""
	# Scan s
	i = 0
	n = len(s)
	while i < n:
		if not s[i].isdigit():
			result += s[i]
			i += 1
		else:
			# When we see a digit, keep scanning until we don't see a digit.
			num = ""
			while s[i].isdigit():
				num += s[i]
				i += 1
			num = int(num)
			# Find the matching left and right brackets
			# Count number of left brackets
			bracket_count = 1
			for j in range(i + 1, n):
				if s[j] == '[':
					bracket_count += 1
				elif s[j] == ']':
					bracket_count -= 1
				if bracket_count == 0:
					break # Now j is index of the matching ]
			
			temp = decompress(s[i + 1: j])
			for k in range(num):
				result += temp
			
			i = j + 1
	return result

def test_decompress(s: str):
	print(f"Compressed string: {s}")
	s_decomp = decompress(s)
	print(f"Decompressed string: {s_decomp}")

def main():
	test_decompress("ab3[c2[x2[pq]y3[uv]z]d]ed")
	test_decompress("abcdefgh")
	test_decompress("ab3[cd]ef2[xyz]w")
	test_decompress("3[3[m]]") 
	test_decompress("a1[b]1[c]2[d]1[e]5[f]") 
	test_decompress("2[ab]3[c2[de]f]1[gh]3[ij]") 
	test_decompress("")
	test_decompress("10[a]")
	test_decompress("ab12[c]4[de]f15[g]")
	test_decompress("10[10[x]]")
	test_decompress("qw3[15[e]]r10[t]yu2[i]o20[p]")

if __name__ == '__main__':
	main()
