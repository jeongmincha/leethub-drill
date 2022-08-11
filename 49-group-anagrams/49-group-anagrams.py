class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        
        for s in strs:
            counter = {}
            for c in s:
                counter[c] = 1 + counter.get(c, 0)
            
            key = ''.join([''.join(map(str, item)) for item in sorted(counter.items())])
            
            l = h.get(key, [])
            l.append(s)
            h[key] = l
        
        return list(h.values())
            
