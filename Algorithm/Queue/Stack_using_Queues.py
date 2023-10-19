# 큐를 이용한 스택 구현

import collections
class MyStack:

    def __init__(self):
        self.q = collections.deque()    

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        return self.q.popleft()
        
    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        itm = self.stack[-1]
        print(itm)
        self.stack.pop()
        return itm

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) != 0:
            return False
        else:
            return True


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)

param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)