class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [1] * N
        right = [1] * N
        left[0] = nums[0]
        right[-1] = nums[-1]
        
        for i in range(1, N):
            left[i] = nums[i] * left[i-1]
        
        for i in range(N-2, -1, -1):
            right[i] = nums[i] * right[i+1]
        
        print(left, right)
        
        answer = [right[1]]
        for i in range(1, N-1):
            answer.append(left[i-1] * right[i+1])
        answer.append(left[N-2])
        
        return answer