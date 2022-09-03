class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1: {} -> {}, {1}
        # 2: {},{2}, {1},{1,2}
        # 3: {},{3}, {2},{2,3}, {1}, {1,3}, {1,2}, {1,2,3} => 8 cases
        
        N = len(nums)
        answer = [[], [nums[0]]]
        
        for i in range(1, N):
            num = nums[i]
            previous_answer = answer[:] # copy without reference
            for e in previous_answer:
                answer.append(e + [])
                answer.append(e + [num])
            
            answer = answer[2 ** i:] # remove the previous duplicate answers
        
        return answer