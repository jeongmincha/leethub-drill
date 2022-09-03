class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0
        stack = [] # (starting index, height)
        
        for current_i, current_h in enumerate(heights):
            starting_i = current_i
            
            while stack and stack[-1][1] >= current_h:
                i, h = stack.pop()
                answer = max(answer, h * (current_i - i))
                starting_i = i

            stack.append((starting_i, current_h))
            
        for i, h in stack:
            answer = max(answer, h * (len(heights) - i))
        
        return answer
            