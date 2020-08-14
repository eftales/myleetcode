class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ["{","[","("]

        def opposit(c):
            if c == ")":
                return "("
            elif c == "]":
                return "["
            elif c == "}":
                return "{"

        for each in s:
            if len(stack) == 0:
                if each in left:
                    stack.append(each)
                    continue
                else:
                    return False

            if each in left:
                stack.append(each)
            else:
                if stack[-1] == opposit(each):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


s = Solution()
s.isValid("()")