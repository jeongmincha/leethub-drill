class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        
        counterP = [0] * 26
        for c in p:
            counterP[ord(c) - ord('a')] += 1
        
        counter = [0] * 26
        for c in s[:len(p)]:
            counter[ord(c) - ord('a')] += 1
        
        if tuple(counterP) == tuple(counter):
            answer.append(0)
        
        l = 0
        for r in range(len(p), len(s)):
            counter[ord(s[r]) - ord('a')] += 1
            counter[ord(s[l]) - ord('a')] -= 1
            l += 1
            
            if tuple(counterP) == tuple(counter):
                answer.append(l)
        
        return answer
                