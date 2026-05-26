class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        perm = []
        def backtrack(i):
            if i>=len(s):
                res.append(perm.copy())
                return

            for j in range(i, len(s)):
                if self.ispal(s[i:j+1]):
                    perm.append(s[i:j+1])
                    backtrack(j+1)
                    perm.pop()
        backtrack(0)
        return res
    def ispal(self, s):
        return s==s[::-1]