class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[len(s)]=True

        for c in range(len(s), -1, -1):
            for w in wordDict:
                if c+len(w) <= len(s) and s[c:c+len(w)]==w:
                    dp[c] = dp[c+len(w)]
                if dp[c]:
                    break
        return dp[0]