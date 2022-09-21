class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_set = sum(set(nums))
        sum_all = sum(nums)
        
        return 2 * sum_set - sum_all
        
            