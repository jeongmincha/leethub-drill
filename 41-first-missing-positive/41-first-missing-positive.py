class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        
        for i in range(N):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(N):
            val = abs(nums[i])
            if 1 <= val <= N:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -(N+1)

        for i in range(1, N+1):
            if nums[i-1] >= 0:
                return i
        
        return N+1
                