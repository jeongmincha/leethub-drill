class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        answer = []
        s_counter = [0] * 26
        p_counter = [0] * 26
        
        for pc in p:
            p_counter[ord(pc) - ord('a')] += 1
        
        for sc in s[:len(p)]:
            s_counter[ord(sc) - ord('a')] += 1
        
        if tuple(s_counter) == tuple(p_counter):
            answer.append(0)
        
        for start in range(1, len(s) - len(p) + 1):
            s_counter[ord(s[start-1]) - ord('a')] -= 1
            s_counter[ord(s[start+len(p)-1]) - ord('a')] += 1
            
            if tuple(s_counter) == tuple(p_counter):
                answer.append(start)
        
        return answer