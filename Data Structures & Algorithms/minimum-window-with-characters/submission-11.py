class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        window, countT = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)

        minL,minR = 0, 0
        minlen = float("infinity")

        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in countT:
                window[char] = 1+window.get(char, 0)

                if window[char] == countT[char]:
                    have += 1
            while have==need:
                if r-l+1 < minlen:
                    minlen = r-l+1
                    minL, minR = l, r
                if s[l] in countT:
                    window[s[l]]-=1
                    if window[s[l]] < countT[s[l]]: 
                        have -=1
                l+=1
        res = s[minL:minR+1]
        return res if minlen<float("infinity") else ""