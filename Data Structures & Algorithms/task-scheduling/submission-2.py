class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) - 1
        heap = list(count.values())
        heapq.heapify(heap)

        q = deque()

        while heap or q:
            time += 1
            if heap:
                task = heapq.heappop(heap)+1
                if task != 0:
                    q.append((task, time+n))
            if q and q[0][1] <= time:
                task, _ = q.popleft()
                heapq.heappush(heap, task)
        return time

            
            