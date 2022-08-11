class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        
        counterT = {}
        for c in t:
            counterT[c] = 1 + counterT.get(c, 0)
        counterWindow = {}
        
        res, resLen = [-1,-1], float("infinity")
        have, need = 0, len(counterT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            counterWindow[c] = 1 + counterWindow.get(c, 0)
            
            if c in counterT and counterT[c] == counterWindow[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                counterWindow[s[l]] -= 1
                if s[l] in counterT and counterWindow[s[l]] < counterT[s[l]]:
                    have -= 1
                l += 1
        
        if resLen == float("infinity"):
            return ""
        else:
            return s[res[0]:res[1]+1]
        
        
        