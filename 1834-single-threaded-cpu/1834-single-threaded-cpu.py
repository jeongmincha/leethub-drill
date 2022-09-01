import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, task in enumerate(tasks):
            task.append(idx)
        # tasks = [(1,2,0),(2,4,1),(3,2,2),(4,1,3)]
        
        tasks.sort(key=lambda e: e[0]) # sort by enqueueTime
        
        idx = 0
        time = tasks[0][0] # the minimum enqueTime
        answer = []
        minHeap = []
        
        while minHeap or idx < len(tasks):
            # find the possible tasks at a certain 'time'
            while idx < len(tasks) and time >= tasks[idx][0]:
                enqueueTime, processTime, index = tasks[idx]
                heapq.heappush(minHeap, (processTime, index))
                idx += 1
            
            if minHeap:
                processTime, index = heapq.heappop(minHeap)
                time += processTime
                answer.append(index)
            else:
                time = tasks[idx][0]
        
        return answer
        
        
        