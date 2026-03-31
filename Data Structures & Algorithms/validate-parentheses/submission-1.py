class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if stack and c in d and d[c]==stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True
        