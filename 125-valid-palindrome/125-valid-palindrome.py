class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([e.lower() for e in s if e.isalpha() or e.isdigit()])
        
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
                break

            l += 1
            r -= 1
        
        return True