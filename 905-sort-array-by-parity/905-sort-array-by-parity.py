class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last_even_idx = 0
        for idx, num in enumerate(nums):
            if num % 2 == 0:
                [nums[idx], nums[last_even_idx]] = [nums[last_even_idx], nums[idx]]
                last_even_idx += 1
        
        return nums