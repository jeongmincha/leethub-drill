"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)
        
        intervals.sort(key=lambda x: x.start) # sort by starting time
        
        answer = []
        last_end = intervals[0].end
        for i in range(len(intervals)):
            curr = intervals[i]
            
            if curr.start > last_end:
                answer.append(Interval(last_end, curr.start))
            
            last_end = max(last_end, curr.end)
        
        return answer