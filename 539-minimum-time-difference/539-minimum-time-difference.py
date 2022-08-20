class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(str):
            hour, minutes = list(map(int, str.split(":")))
            return hour * 60 + minutes
        
        times = []
        for timePoint in timePoints:
            times.append(convert(timePoint))
        
        times.sort()
        
        answer = 1440
        for i in range(len(times)):
            p = times[(i+1) % len(times)]
            n = times[i]
            if p == n:
                return 0

            diff = abs(n-p)
            answer = min(answer, diff, abs(1440-diff))
        
        return answer