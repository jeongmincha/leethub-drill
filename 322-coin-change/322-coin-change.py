class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # f(amount) = the answer of the problem
        # f(1) = 1, f(2) = 1, f(5) = 1 => base cases
        # bottom-up approach of dynamic programming
        # f(n) = min(f(n-1)+1, f(n-2)+1, f(n-5)+1)
        # f(n) = -1 when f(n-1), f(n-2), f(n-5) cannot be made.
        # time complexity = O(n*k) <= n: amount, k: # of coins
        
        if amount == 0:
            return 0
        
        memo = [0] * (amount+1)

        for current_amount in range(1, amount+1):
            possible = []
            for coin in coins:
                if current_amount - coin >= 0 and memo[current_amount-coin] >= 0:
                    possible.append(memo[current_amount-coin] + 1)
            
            if len(possible) == 0:
                memo[current_amount] = -1
            else:
                memo[current_amount] = min(possible)
        
        return memo[amount]