class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if stack and c == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif stack and c == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()
            elif stack and c == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        return True