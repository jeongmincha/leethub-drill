class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        return N * (N+1) // 2 - sum(nums)