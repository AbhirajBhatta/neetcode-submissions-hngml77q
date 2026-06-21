class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()

        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, hashset, prev):
            if (r<0 or c<0 or
                r==rows or c==cols or
                (r, c) in hashset or
                prev > heights[r][c]):
                return
            hashset.add((r, c))
            dfs(r-1, c, hashset, heights[r][c])
            dfs(r+1, c, hashset, heights[r][c])
            dfs(r, c-1, hashset, heights[r][c])
            dfs(r, c+1, hashset, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols-1, atl, 0)

        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows-1, c, atl, 0)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res