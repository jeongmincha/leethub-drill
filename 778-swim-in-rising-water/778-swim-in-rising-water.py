import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        MAX_VALUE = 2500
        moves = [[-1,0],[1,0],[0,-1],[0,1]]
        
        N = len(grid) - 1
        x, y = 0, 0
        min_heap = []
        answer = grid[0][0]
        
        while x < N or y < N:
            for move_x, move_y in moves:
                new_x = x + move_x
                new_y = y + move_y
                
                if new_x < 0 or new_x > N or new_y < 0 or new_y > N or grid[new_x][new_y] > MAX_VALUE:
                    continue
                
                heapq.heappush(min_heap, (grid[new_x][new_y], new_x, new_y))
                grid[new_x][new_y] = MAX_VALUE
            
            _next = heapq.heappop(min_heap)
            answer = max(answer, _next[0])
            x = _next[1]
            y = _next[2]
        
        return answer
                    