class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            if self.minstack[-1] >= val:
                self.minstack.append(val)

    def pop(self) -> None:
        p = self.stack.pop()
        if p == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
