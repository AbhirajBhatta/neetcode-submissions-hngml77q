class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n

        for i in range(m-1):
            temp = [1]*n
            for j in range(n-2, -1, -1):
                temp[j] = temp[j+1] + row[j]
            row = temp
        return row[0]

