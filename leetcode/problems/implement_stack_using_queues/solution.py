class MyStack:

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l.insert(0,x)

    def pop(self) -> int:
        a = self.l[0]
        self.l.remove(self.l[0])
        return a

    def top(self) -> int:
        return self.l[0]

    def empty(self) -> bool:
        if len(self.l) == 0: return True
        else: return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()