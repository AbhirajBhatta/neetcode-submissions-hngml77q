class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        visited = set()
        minheap = [[grid[0][0], 0, 0]]
        visited.add((0, 0))
        def travers(cost, r, c):
            if (r<0 or c<0 or
                (r, c) in visited or 
                r==N or c==N):
                return
            visited.add((r, c))
            heapq.heappush(minheap, [max(cost, grid[r][c]), r, c])
        
        while minheap:
            cost, r, c = heapq.heappop(minheap)
            if r==N-1 and c==N-1:
                return cost
            
            travers(cost, r-1, c)
            travers(cost, r+1, c)
            travers(cost, r, c-1)
            travers(cost, r, c+1)
        
