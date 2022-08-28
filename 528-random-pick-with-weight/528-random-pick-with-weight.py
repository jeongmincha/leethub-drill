import random

class Solution:
    def __init__(self, w: List[int]):
        # prefix sum of weights [1,3] -> [0.25, 1]
        _sum = sum(w)
        self.prefixSum = [w[0]]
        for i in range(len(w) - 1):
            self.prefixSum.append(self.prefixSum[-1] + w[i+1])
        
        self.prefixSum = [e / _sum for e in self.prefixSum]

    def pickIndex(self) -> int:
        rand = random.random() # 0~1
        
        left = 0
        right = len(self.prefixSum)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid == 0:
                if 0 < rand <= self.prefixSum[0]:
                    return 0
                else:
                    left = mid + 1
            else:
                if self.prefixSum[mid-1] < rand <= self.prefixSum[mid]:
                    return mid
                elif rand <= self.prefixSum[mid-1]:
                    right = mid - 1
                elif rand > self.prefixSum[mid]:
                    left = mid + 1
        
        return -1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()