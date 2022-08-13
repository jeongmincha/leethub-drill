class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 0
        curr_num_ones = 0
        num_continuous_ones = []
        allow_zero = False
        
        for num in nums:
            
            if num == 1:
                curr_num_ones += 1
                allow_zero = True
            else:
                if allow_zero:
                    num_continuous_ones.append(curr_num_ones)
                    num_continuous_ones = num_continuous_ones[-2:]
                    answer = max(answer, sum(num_continuous_ones))
                    curr_num_ones = 0
                    allow_zero = False
                else:
                    curr_num_ones = 0
                    num_continuous_ones = []
        
        if curr_num_ones == len(nums):
            return curr_num_ones - 1
        
        if curr_num_ones > 0:
            num_continuous_ones.append(curr_num_ones)
            num_continuous_ones = num_continuous_ones[-2:]
            answer = max(answer, sum(num_continuous_ones))
        
        return answer
                    
                
                
            
            