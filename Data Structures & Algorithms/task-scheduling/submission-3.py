class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = {}
        for t in tasks:
            taskMap[t] = 1+taskMap.get(t, 0)
        
        q = deque()
        maxH = [-v for v in taskMap.values()]
        heapq.heapify(maxH)

        t = 0
        while q or maxH:
            t+=1
            if maxH:
                task = heapq.heappop(maxH)+1
                if task!=0:
                    q.append([task, t+n])
            if q:
                if q[0][1]==t:
                    heapq.heappush(maxH, q.popleft()[0])
        return t
