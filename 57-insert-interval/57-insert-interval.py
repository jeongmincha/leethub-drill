class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        
        for idx, interval in enumerate(intervals):
            if newInterval[1] < interval[0]: # end of overlapping
                answer.append(newInterval)
                answer.extend(intervals[idx:])
                return answer
            elif newInterval[0] > interval[1]: # still not overlapped
                answer.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        answer.append(newInterval)
        return answer