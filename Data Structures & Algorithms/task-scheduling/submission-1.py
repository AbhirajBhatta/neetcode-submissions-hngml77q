from _heapq import heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = 1 + counts.get(task, 0)
        time = 0
        heap = [-val for val in counts.values()]
        heapq.heapify(heap)
        q = deque()
        while heap or q:
            time+=1

            if heap:
                timeleft = heapq.heappop(heap) + 1
                if timeleft!=0:
                    q.append([timeleft, time+n])
            
            if q and time == q[0][1]:
                    heapq.heappush(heap, q.popleft()[0])
        return time


