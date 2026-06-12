class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispal(s):
            l, r = 0, len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        res = []
        
        def find(i, curStr):
            if i==len(s):
                res.append(curStr.copy())
                return
            for j in range(i, len(s)):
                if ispal(s[i:j+1]):
                    curStr.append(s[i:j+1])
                    find(j+1, curStr)
                    curStr.pop()
        find(0, [])
        return res
        
