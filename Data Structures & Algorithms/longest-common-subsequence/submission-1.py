class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        grid = [[0]*(m+1) for i in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i]==text2[j]:
                    grid[i][j] = 1+ grid[i+1][j+1]
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        return grid[0][0]
