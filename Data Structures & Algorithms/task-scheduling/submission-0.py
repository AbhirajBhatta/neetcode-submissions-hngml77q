class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1+ count.get(task, 0)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        t = 0
        q = deque() # contains pair [remaining time, curr time]

        while heap or q:
            t+=1

            if heap:
                timeLeft = heapq.heappop(heap) + 1
                if timeLeft:
                    q.append([timeLeft, t+n])
            
            if q and q[0][1] == t:
                newTask = q.popleft()[0]
                heapq.heappush(heap, newTask)
        return t