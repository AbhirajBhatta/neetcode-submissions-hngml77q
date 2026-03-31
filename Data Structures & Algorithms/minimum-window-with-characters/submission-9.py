class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        l = 0
        minLen = float("infinity")
        start,end = 0, 0

        tset = {}
        window = {}

        for i in t:
            tset[i] = 1+ tset.get(i, 0)
        have, need = 0, len(tset)

        for r in range(0, len(s)):
            if s[r] in tset:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == tset[s[r]]:
                    have +=1
            while have == need:
                if r-l+1 < minLen:
                    start, end = l, r
                    minLen = min(minLen, r-l+1)
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] <tset[s[l]]:
                        have -= 1
                l+=1
            
        res = s[start:end+1]
        return res if minLen!=float("infinity") else ""
            