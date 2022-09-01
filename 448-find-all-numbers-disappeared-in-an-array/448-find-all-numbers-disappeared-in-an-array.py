class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            curr_num = abs(nums[i]) - 1
            nums[curr_num] = min(nums[curr_num], -nums[curr_num])
        
        return [i+1 for i in range(N) if nums[i] > 0]