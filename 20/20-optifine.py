class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False

        stack = []
        pairs = {
            "}":"{",
            "]":"[",
            ")":"("
            }

        for each in s:
            if each in pairs:
                if not stack or stack[-1] != pairs[each]:
                    return False
                stack.pop()
            else:
                stack.append(each)
        if not stack:
            return True
        return False

