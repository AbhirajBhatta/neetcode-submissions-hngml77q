class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        p, a = set(), set()

        def dfs(r, c, hashSet, prevHeight):
            if (r<0 or c<0 or r==rows or c==cols or
                (r, c) in hashSet or heights[r][c] < prevHeight):
                return
            hashSet.add((r, c))
            dfs(r+1, c, hashSet, heights[r][c])
            dfs(r-1, c, hashSet, heights[r][c])
            dfs(r, c-1, hashSet, heights[r][c])
            dfs(r, c+1, hashSet, heights[r][c])
        for r in range(rows):
            dfs(r, 0, p, heights[r][0])
            dfs(r, cols-1, a, heights[r][cols-1])
        for c in range(cols):
            dfs(0, c, p, heights[0][c])
            dfs(rows-1, c, a, heights[rows-1][c])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in p and (r, c) in a:
                    res.append([r, c])
        return res
        