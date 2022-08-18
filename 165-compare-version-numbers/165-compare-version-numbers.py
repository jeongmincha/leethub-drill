class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        maxLen = max(len(v1), len(v2))
        
        if len(v1) < maxLen:
            l1 = len(v1)
            for _ in range(maxLen-l1):
                v1.append(0)
        if len(v2) < maxLen:
            l2 = len(v2)
            for _ in range(maxLen-l2):
                v2.append(0)
        
        for i in range(maxLen):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1

        return 0