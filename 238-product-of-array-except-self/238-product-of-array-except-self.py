class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        answer = [1] * N
        for i in range(N-1):
            answer[i+1] = nums[i] * answer[i]
        
        suffix_product = 1
        for i in range(N-1, -1, -1):
            answer[i] = answer[i] * suffix_product
            suffix_product *= nums[i]
        
        return answer
        