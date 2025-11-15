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
			num = int(s[i])
			# Find the matching left and right brackets
			# Count number of left brackets
			bracket_count = 1
			for j in range(i + 2, n):
				if s[j] == '[':
					bracket_count += 1
				elif s[j] == ']':
					bracket_count -= 1
				if bracket_count == 0:
					break # Now j is index of the matching ]
			
			temp = decompress(s[i + 2: j])
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

if __name__ == '__main__':
	main()
