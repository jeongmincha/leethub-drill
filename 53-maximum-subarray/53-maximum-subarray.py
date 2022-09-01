class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = float('-inf')
        curr_sum = 0
        
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            answer = max(answer, curr_sum)
        
        return answer
            