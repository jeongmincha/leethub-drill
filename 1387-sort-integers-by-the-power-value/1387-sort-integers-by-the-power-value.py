class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        
        def get_power(n):
            original_n = n
            step = 0
            
            while n > 1:
                if n in memo:
                    step += memo[n]
                    break
                
                if n % 2 == 0:
                    n //= 2
                else:
                    n = n * 3 + 1
                
                step += 1
            
            memo[original_n] = step
            return step
    
        return sorted(range(lo, hi+1), key=get_power)[k-1]