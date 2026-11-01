from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)

        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        if self.empty():
            return -1
        return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            return -1
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


if __name__ == "__main__":
    sol = MyStack()

    sol.push(1)
    sol.push(2)
    print("Top value: ", sol.top())
    print("Pop value: ", sol.pop())
    print("Is Empty: ", sol.empty())
