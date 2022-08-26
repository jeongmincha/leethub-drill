class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if target < nums[0]:
            return [-1, -1]
        if target > nums[-1]:
            return [-1, -1]
        
        # binary search
        answer = [-1, -1]
        
        N = len(nums)
        left = 0
        right = N-1
        
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid-1] < target) and nums[mid] == target:
                answer[0] = mid
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        left = 0
        right = N-1
        while left <= right:
            mid = (left + right) // 2
            if (mid == N-1 or nums[mid+1] > target) and nums[mid] == target:
                answer[1] = mid
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return answer