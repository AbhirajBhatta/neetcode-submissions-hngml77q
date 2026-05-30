class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []

        combinations = []

        def dfs(i):
            if i==len(digits):
                res.append("".join(combinations.copy()))
                return
            d = digits[i]
            for c in phone_map[d]:
                combinations.append(c)
                dfs(i+1)
                combinations.pop()
        if digits:
            dfs(0)
        return res