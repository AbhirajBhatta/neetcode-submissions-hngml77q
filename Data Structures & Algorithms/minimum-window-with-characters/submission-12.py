class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ""

        countT, countS = {}, {}
        
        for c in t:
            countT[c] = 1+countT.get(c, 0)
        have, need = 0, len(countT)
        l = 0
        minLen = float("inf")
        minL, minR = 0, 0
        for r in range(len(s)):
            c = s[r]
            if c in countT:
                countS[c] = 1+countS.get(c, 0)
                if countT[c]==countS[c]:
                    have+=1
            while have==need:
                if (r-l+1)<minLen:
                    minLen = r-l+1
                    minL = l
                    minR = r
                if s[l] in countS:
                    countS[s[l]] -= 1
                    if countS[s[l]] < countT[s[l]]: have-=1
                    if countS[s[l]]==0: del countS[s[l]]
                l+=1
            
        res = s[minL:minR+1]
        return res if minLen!=float("inf") else ""
        