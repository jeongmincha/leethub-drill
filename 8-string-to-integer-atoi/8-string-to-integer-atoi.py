class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        
        sign = 1
        num = 0
        idx = 0
        
        while idx < len(s) and s[idx] == " ":
            idx += 1
        
        if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
            sign = -1 if s[idx] == '-' else 1
            idx += 1
        
        while idx < len(s) and s[idx].isdigit():
            num *= 10
            num += ord(s[idx]) - ord('0')
            idx += 1
        
        if sign > 0:
            return min(num * sign, 2 ** 31-1)
        else:
            return max(num * sign, -2 ** 31)
