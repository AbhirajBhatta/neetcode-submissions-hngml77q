class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }   
        if not digits:
            return []
        res = []

        current = []
        def make(i):
            if i==len(digits):
                res.append("".join(current))
                return
            dig = digits[i]
            for c in phoneMap[dig]:
                current.append(c)
                make(i+1)
                current.pop()
        make(0)
        return res