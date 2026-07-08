class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            counts[c] = 1+counts.get(c, 0)
            while (r-l+1) - max(counts.values()) > k:
                counts[s[l]] -=1
                if counts[s[l]]==0:
                    counts.pop(s[l])
                l+=1
            res = max(res, r-l+1)
            
        return res