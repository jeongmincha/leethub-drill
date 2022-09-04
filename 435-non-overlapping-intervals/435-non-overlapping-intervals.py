class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda k: k[1])
        removed, last_end = 0, float('-inf')
        for start, end in intervals:
            if start < last_end:
                removed += 1
            else:
                last_end = end
        return removed