import heapq
from collections import defaultdict, deque


class Solution:
    def least_interval(self, tasks: list[str], n: int) -> int:
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        priority_queue: list[int] = [-ctn for ctn in task_count.values()]
        heapq.heapify(priority_queue)

        timer = 0
        cooldown_task: deque[tuple[int, int]] = deque()

        while cooldown_task or priority_queue:
            timer += 1

            if cooldown_task and cooldown_task[0][-1] < timer:
                task = cooldown_task.popleft()
                heapq.heappush(priority_queue, -task[0])

            if priority_queue:
                task = -heapq.heappop(priority_queue)
                task -= 1

                if task > 0:
                    cooldown_task.append((task, timer + n))

        return timer


if __name__ == "__main__":
    sol = Solution()

    print(f"Final Output is: {sol.least_interval(['A', 'A', 'A', 'B', 'B', 'B'], 2)}")
    print(f"Final Output is: {sol.least_interval(['A', 'C', 'A', 'B', 'D', 'B'], 1)}")
    print(f"Final Output is: {sol.least_interval(['A', 'A', 'A', 'B', 'B', 'B'], 3)}")
    print(
        f"Final Output is: {sol.least_interval(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'E'], 2)}"
    )
