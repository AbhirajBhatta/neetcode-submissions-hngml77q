class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def baktrack(i, curPals):
            if i==len(s):
                res.append(curPals.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    curPals.append(s[i:j+1])
                    baktrack(j+1, curPals)
                    curPals.pop()
        baktrack(0, [])
        return res
                
    
