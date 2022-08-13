class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        answer = 0
        lastEnd = intervals[0][1]
        for interval in intervals[1:]:
            if lastEnd <= interval[0]:
                lastEnd = interval[1]
            else:
                answer += 1
                lastEnd = min(interval[1], lastEnd)
        
        return answer