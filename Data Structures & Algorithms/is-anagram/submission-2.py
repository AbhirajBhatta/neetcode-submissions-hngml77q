class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = {}
        check2 = {}

        for c in s:
            check1[c] = 1 + check1.get(c, 0)
        for c in t:
            check2[c] = 1 + check2.get(c, 0)
        if (check1==check2):
            return True
        else:
            return False
