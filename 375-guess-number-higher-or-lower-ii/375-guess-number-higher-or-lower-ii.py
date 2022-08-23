class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        # memo[i][j] = the minimum amount of money to win when we pick a number between [i, j]
        # memo[2][3] = 2
        # memo[2][2] = 0 # no need to pay anymore
        memo = [[0] * (n+1) for _ in range(n+1)] 
        
        for i in range(1, n):
            memo[i][i+1] = i
        
        for length in range(3, n+1):
            for i in range(1, n-length+2):
                cost = float("inf")
                j = i + length - 1
                
                for pivot in range(i, j+1):
                    # pivot + max(memo[i][pivot-1], memo[pivot+1][j])
                    possibles = [0]
                    if i <= pivot-1:
                        possibles.append(memo[i][pivot-1])
                    if pivot+1 <= j:
                        possibles.append(memo[pivot+1][j])
                    cost = min(cost, pivot + max(possibles))
                        
                memo[i][j] = cost
        
        return memo[1][n]
        
        
        