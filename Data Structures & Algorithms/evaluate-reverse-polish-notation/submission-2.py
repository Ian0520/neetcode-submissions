class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == '+':
                a = int(s.pop())
                b = int(s.pop())
                result = a + b
                s.append(result)
            elif t == '-':
                a = int(s.pop())
                b = int(s.pop())
                result = b-a
                s.append(result)
            elif t == '*':
                a = int(s.pop())
                b = int(s.pop())
                result = a * b
                s.append(result)
            elif t == '/':
                a = int(s.pop())
                b = int(s.pop())
                result = b/a
                s.append(result)
            else:
                s.append(t)

        return int(s[0])