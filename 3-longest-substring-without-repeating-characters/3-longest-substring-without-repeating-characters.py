class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        answer = 0
        left = 0
        last_index = {}
        
        for right, char in enumerate(s):
            # char in last_index -> there is a duplicates
            # left <= last_index[char] -> there is a duplicates "in current sliding window"
            if char in last_index and left <= last_index[char]:
                left = last_index[char] + 1
            else:
                answer = max(answer, right - left + 1)
            
            last_index[char] = right
        
        return answer
                