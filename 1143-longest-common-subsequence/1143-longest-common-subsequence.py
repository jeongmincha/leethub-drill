class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   a b c d e
        # a 1 1 1 1 1
        # c 1 1 2 2 2
        # e 1 1 2 2 3
        
        # f(i1, i2) = f(i1-1, i2-1) + 1 if text1[i1] == text2[i2]
        # f(i1, i2) = max(f(i1-1, i2), f(i1, i2-1)) otherwise
        # f(0, x) = 0, f(x, 0) = 0
        
        L1 = len(text1)
        L2 = len(text2)
        
        memo = [[0] * (L2+1) for _ in range(L1+1)] # L1+1 * L2+1
        
        for i1 in range(1, L1+1):
            for i2 in range(1, L2+1):
                if text1[i1-1] == text2[i2-1]:
                    memo[i1][i2] = memo[i1-1][i2-1] + 1
                else:
                    memo[i1][i2] = max(memo[i1-1][i2], memo[i1][i2-1])
        
        return memo[-1][-1]
        
        