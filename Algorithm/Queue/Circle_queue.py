class MyCircularQueue:

    def __init__(self, k: int):
        self.circular_queue = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.circular_queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.circular_queue.pop(0)
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.circular_queue[0]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.circular_queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.circular_queue) == 0

    def isFull(self) -> bool:
        return len(self.circular_queue) == self.k