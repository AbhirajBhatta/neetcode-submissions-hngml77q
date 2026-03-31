class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingMap = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in closingMap:
                if stack and stack[-1]==closingMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
