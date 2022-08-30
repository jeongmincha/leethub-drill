import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        S = len(servers)
        T = len(tasks)
        answer = []
        
        available = [(servers[idx], idx) for idx in range(S)] # (weight, index)
        heapq.heapify(available) # we compare first value
        unavailable = []
        
        t = 0
        for i in range(T):
            t = max(t, i)
            
            # warp to the time which at least one server will be available
            if len(available) == 0:
                t = unavailable[0][0]
            
            while unavailable and t >= unavailable[0][0]:
                timefree, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            
            weight, index = heapq.heappop(available)
            answer.append(index)
            
            heapq.heappush(unavailable, (t + tasks[i], weight, index))
        
        return answer
            
            
        