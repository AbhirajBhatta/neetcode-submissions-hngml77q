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

        res = []

        def backtrack(i, curWord):
            if i==len(digits):
                res.append("".join(curWord))
                return
            digit = digits[i]
            for c in phoneMap[digit]:
                curWord.append(c)
                backtrack(i+1, curWord)
                curWord.pop()
        backtrack(0, [])
        return res if digits else []