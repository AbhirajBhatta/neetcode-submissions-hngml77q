class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        maxH = []
        for c in count.values():
            maxH.append(-1*c)
        heapq.heapify(maxH)

        q = deque()
        time = 0
        while q or maxH:
            if maxH:
                task = heapq.heappop(maxH) + 1
                cooldown = time + n
                if task < 0:
                    q.append([task, cooldown])
            if q:
                if q[0][1]==time:
                    task, _ = q.popleft()
                    heapq.heappush(maxH, task)
                
            time+=1
        return time