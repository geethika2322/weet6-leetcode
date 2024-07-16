class MyCircularQueue:

    def _init_(self, k: int):
        self.queue = [-1] * k
        self.front = self.rear = -1
        self.size = 0  #current size of the queue
        self.maxsize = k #max size of the queue

    def enQueue(self, value: int) -> bool:
        if self.front == -1:
            self.front = 0
        if self.size < self.maxsize:
            self.rear = (self.rear + 1) % self.maxsize # for making it circular
            self.queue[self.rear] = value
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.size > 0:
            self.front = (self.front + 1) % self.maxsize # for making it circular
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        return self.queue[self.front] if self.size > 0 else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size > 0 else -1

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.maxsize else False
