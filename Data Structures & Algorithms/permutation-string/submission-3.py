class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        key = [0]*26
        for c in s1:
            key[ord(c)-ord("a")] += 1
        for l in range(len(s2)-len(s1)+1):
            check = [0]*26
            for r in range(l, l+len(s1)):
                check[ord(s2[r])-ord("a")] += 1
            if key==check:
                return True
        return False