class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        for col in range(n):
            if grid[0][col] == 1:
                for row in range(m):
                    grid[row][col] = 1 - grid[row][col]
        
        for row in range(m):
            _sum = 0
            for col in range(n):
                _sum += grid[row][col]
            
            if _sum != 0 and _sum != n:
                return False
        
        return True