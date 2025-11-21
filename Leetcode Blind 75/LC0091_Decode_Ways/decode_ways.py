class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0
        n = len(s)
        T = [0] * n # T[i] = number of valid ways to decode s up to index i (inclusive)
        # base case
        T[0] = 1
        # recurrence
        for i in range(1, n):
            if int(s[i]) == 0:
                #print(f"s[i] == 0")
                if int(s[i - 1]) < 1 or int(s[i - 1]) > 2:
                    return 0
                elif i == 1:
                    #print("i = 1 case")
                    T[i] = 1
                else:
                    T[i] = T[i - 2]
            elif int(s[i - 1]) == 0:
                T[i] = T[i - 1]
            elif int(s[i - 1]) < 2:
                if i == 1:
                    T[i] = T[i - 1] + 1
                else:
                    T[i] = T[i - 1] + T[i - 2]
            elif int(s[i - 1]) == 2:
                if int(s[i]) <= 6:
                    if i == 1:
                        T[i] = T[i - 1] + 1
                    else:
                        T[i] = T[i - 1] + T[i - 2]
                else:
                    T[i] = T[i - 1]
            else: # s[i - 1] >= 3
                if int(s[i]) == 0:
                    return 0
                T[i] = T[i - 1]
        #print(T)
        return T[n - 1]