class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        sub = []

        def backtrack(i):
            if i==len(s):
                res.append(sub.copy())
                return
            for j in range(i, len(s)):
                if self.isPal(s[i:j+1]):
                    sub.append(s[i:j+1])
                    backtrack(j+1)
                    sub.pop()
        backtrack(0)
        return res
    def isPal(self, word):
        return word==word[::-1]
