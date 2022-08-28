class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        M = len(mat)
        N = len(mat[0])
        
        dp = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(M)] # M * N * 4
        # dp[x][y][0] = the length of the line until (x,y) in horizontal line (to the right)
        # dp[x][y][1] = the length of the line until (x,y) in vertical line (to the bottom)
        # dp[x][y][2] = the length of the line until (x,y) in diagonal line (diagonal to the right bottom)
        # dp[x][y][3] = the length of the line until (x,y) in anti-diagonal line (diagonal to the left bottom)
        
        answer = 0
        for r in range(M):
            for c in range(N):
                if mat[r][c] == 0:
                    continue
                
                dp[r][c][0] = dp[r][c][1] = dp[r][c][2] = dp[r][c][3] = mat[r][c]
                if r > 0:
                    dp[r][c][0] = dp[r-1][c][0] + 1
                if c > 0:
                    dp[r][c][1] = dp[r][c-1][1] + 1
                if r > 0 and c > 0:
                    dp[r][c][2] = dp[r-1][c-1][2] + 1
                if r > 0 and c < N-1:
                    dp[r][c][3] = dp[r-1][c+1][3] + 1

                answer = max(answer, dp[r][c][0])
                answer = max(answer, dp[r][c][1])
                answer = max(answer, dp[r][c][2])
                answer = max(answer, dp[r][c][3])
        
        return answer
                
                
        