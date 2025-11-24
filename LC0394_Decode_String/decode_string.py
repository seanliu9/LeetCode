class Solution:
    def decodeString(self, s: str) -> str:
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
                
                temp = self.decodeString(s[i + 1: j])
                for k in range(num):
                    result += temp
                
                i = j + 1
        return result