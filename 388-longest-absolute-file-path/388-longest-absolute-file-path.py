class Solution:
    def lengthLongestPath(self, input: str) -> int:
        names = input.split("\n")
        curL, maxL = 0, 0
        stack = []
        
        for name in names:
            name = name.split("\t")
            tabs, name = len(name) - 1, name[-1]
            
            while len(stack) > tabs:
                curL -= len(stack.pop())
                
            curL += len(name)
            stack.append(name)

            if "." in stack[-1]:
                maxL = max(maxL, curL + len(stack) - 1)
                
        return maxL