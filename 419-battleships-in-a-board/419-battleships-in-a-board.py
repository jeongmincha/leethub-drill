class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        DIRECTIONS = [(1,0), (0,1)]
        M = len(board)
        N = len(board[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        
        for x in range(M):
            for y in range(N):
                if board[x][y] == '.':
                    visited[x][y] = True
        
        def dfs(pos, direction): # pos = (x, y), direction = (dx, dy) # (1,2), (-1,0)
            nonlocal visited
            if pos[0] < 0 or pos[0] >= M or pos[1] < 0 or pos[1] >= N or visited[pos[0]][pos[1]]:
                return
            
            visited[pos[0]][pos[1]] = True
            nx, ny = pos[0] + direction[0], pos[1] + direction[1]
            dfs((nx, ny), direction)
        
        answer = 0
        for x in range(M):
            for y in range(N):
                if visited[x][y]:
                    continue
                
                for direction in DIRECTIONS:
                    visited[x][y] = False
                    dfs((x,y), direction)
                
                visited[x][y] = True
                answer += 1

        return answer