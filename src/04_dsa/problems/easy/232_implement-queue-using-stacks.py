class MyQueue:
    def __init__(self):
        self.st_1 = []
        self.st_2 = []

    def push(self, x: int) -> None:
        self.st_2.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1

        if not self.st_1:
            while self.st_2:
                self.st_1.append(self.st_2.pop())

        return self.st_1.pop()

    def peek(self) -> int:
        if self.empty():
            return -1

        if not self.st_1:
            while self.st_2:
                self.st_1.append(self.st_2.pop())

        return self.st_1[-1]

    def empty(self) -> bool:
        return not self.st_1 and not self.st_2


if __name__ == "__main__":
    my_queue = MyQueue()

    my_queue.push(1)
    my_queue.push(2)
    print(f"Top element in queue is: {my_queue.peek()}")
    my_queue.pop()
    print(f"Top element in queue is: {my_queue.peek()}")
    print(f"Is Queue is empty: {my_queue.empty()}")
