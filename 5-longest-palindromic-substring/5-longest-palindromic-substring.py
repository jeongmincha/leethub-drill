class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.answer = None
        self.answerLen = 0
        
        def loop(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > self.answerLen:
                    self.answer = s[left:right+1]
                    self.answerLen = right-left+1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            loop(i, i)
            loop(i, i+1)
        
        return self.answer