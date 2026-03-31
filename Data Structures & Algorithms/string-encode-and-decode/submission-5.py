class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "$" + s
        return res
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while j<len(s):
            while s[j] != "$":
                j+= 1
            l = int(s[i:j])
            i = j+1
            j = i+l
            res.append(s[i:j])
            i = j
            
        return res
