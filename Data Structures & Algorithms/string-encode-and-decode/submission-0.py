class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        for s in strs: 
            codenum = len(s)
            res = res + str(codenum) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
        
            length = int(s[i:j])
            i = j+1
            j = length +i
            final.append(s[i:j])
            i=j

        return final
                    
