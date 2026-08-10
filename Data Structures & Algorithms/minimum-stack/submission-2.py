class MinStack:
    minstack = []
    mini_stack = []
    def __init__(self):
        self.minstack = []
        self.mini_stack = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        
        if not self.mini_stack or val <= self.mini_stack[-1]:
            self.mini_stack.append(val)

    def pop(self) -> None:
        if self.mini_stack[-1] == self.minstack[-1]:
            self.mini_stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.mini_stack[-1]