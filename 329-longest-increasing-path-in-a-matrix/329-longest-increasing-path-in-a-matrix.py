class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        
        STEPS = [(-1,0),(1,0),(0,-1),(0,1)]
        answer = 1
        
        def dfs(x, y):
            nonlocal answer
            nonlocal dp
            
            if dp[x][y]:
                return dp[x][y]
            
            current = matrix[x][y]
            for step in STEPS:
                nx, ny = x + step[0], y + step[1]
                curr_val = matrix[x][y]

                if 0 <= nx < M and 0 <= ny < N and curr_val > matrix[nx][ny]:
                    dp[x][y] = max(dp[x][y], dfs(nx, ny))

            dp[x][y] += 1
            answer = max(answer, dp[x][y])
            
            return dp[x][y]
        
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        for x in range(M):
            for y in range(N):
                dfs(x, y)
        
        return answer