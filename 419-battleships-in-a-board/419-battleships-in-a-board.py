class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        DIRECTIONS = [(1,0), (0,1)]
        M = len(board)
        N = len(board[0])
        
        def dfs(pos):
            nonlocal board
            if pos[0] < 0 or pos[0] >= M or pos[1] < 0 or pos[1] >= N or board[pos[0]][pos[1]] == '.':
                return
            
            board[pos[0]][pos[1]] = '.'
            for direction in DIRECTIONS:
                nx, ny = pos[0] + direction[0], pos[1] + direction[1]
                dfs((nx, ny))
        
        answer = 0
        for x in range(M):
            for y in range(N):
                if board[x][y] == '.':
                    continue
                
                dfs((x,y))
                answer += 1

        return answer