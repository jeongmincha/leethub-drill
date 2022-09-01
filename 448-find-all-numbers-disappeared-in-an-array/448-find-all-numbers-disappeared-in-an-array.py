class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            curr_num = abs(nums[i]) - 1
            if nums[curr_num] > 0:
                nums[curr_num] *= -1
        
        answer = []
        for i in range(N):
            if nums[i] > 0:
                answer.append(i+1)
        
        return answer