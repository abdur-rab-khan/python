"""
🟡 "asyncio" in Python is used to handle asynchronous jobs using an "event loop", like how "node.js" handles them. It runs tasks in a single thread.
🟡 Unlike node.js, where they have different queues for different tasks, Python has just one queue, the "ready queue", plus a timer list for things like asyncio.sleep().
🟡 "create_task()" just puts the task in the ready queue. It does not run right away. It starts when the current code gives control back to the loop (at an "await" that really waits). When "asyncio.sleep()" time is over, the loop moves the task from the timer list back to the ready queue, and it runs on its turn.

🟡 It has four core things:
    1. coroutine ("async def function gives a coroutine object, it doesn't run until it is awaited or wrapped in a task")
    2. event loop ("runs tasks one by one on a single thread, similar to node.js")
    3. await ("this runs a coroutine inside the current task")
    4. task ("a coroutine wrapped and scheduled by the loop, made with create_task()")

🟡 Important methods in "asyncio":
    1. run(main()): starts the event loop, use it once at the top
    2. create_task(coro): wraps a coroutine in a task, puts it in the ready queue
    3. gather(...): runs many together, gives results in order
    4. TaskGroup(): runs many together, if one fails it cancels the others
    5. wait(tasks): waits for tasks, can stop at FIRST_COMPLETED
    6. as_completed(coros): gives each result as soon as it is ready
    7. sleep(sec): waits without blocking the loop
    8. timeout(sec): raises TimeoutError if the code takes too long
    9. wait_for(coro, sec): older way of timeout
    10. task.cancel(): asks the task to stop at its next await
    11. shield(task): protects a task from outside cancel
    12. to_thread(func, *args): runs blocking code in another thread
    13. Lock, Semaphore, Event, Queue: share data between tasks
"""

import asyncio
import time


async def greet_me():
    print("Calling greet_me function")
    return await asyncio.sleep(5, result="Hello Python")


async def task_1():
    print("Calling task_1 function")
    return await asyncio.sleep(2, result="Task 1 is completed")


async def task_2():
    print("Calling task_2 function")
    raise RuntimeError("Failed to run task_2")


async def task_3():
    print("Calling task_3 function")
    return await asyncio.sleep(2, result="Task 3 is completed")


def block_task(job_name: str, delay):
    now = time.strftime("%H:%M:%S")
    print(f"[{now}, {job_name}]: Calling the block_task function")
    time.sleep(delay)
    return f"{job_name} is done"


async def main():
    # 👉 It's similar to "node.js" where we call a function without using "await" keyword, "create_task" schedule the task so we can run in future.
    without_awaiting_task = asyncio.create_task(greet_me())

    print("Doing some-other tasks")

    # 👉 Similar to node.js "Promise.all", and without "return_exceptions=True", it simply raises the exception but does not stop other tasks to run
    waiting_for_all_task = await asyncio.gather(
        task_1(), task_2(), task_3(), return_exceptions=True
    )
    print("Result of task_1 and task_2: ", waiting_for_all_task)

    # 👉 Using "asyncio.TaskGroup()" simply stop other task once got any exception in the "TaskGroup"
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(task_1())
            tg.create_task(task_2())
            tg.create_task(task_3())
    except ExceptionGroup as e:
        print(f"Error intercepted: {e}")

    # 👉 Using "asyncio.timeout(sec)" raise "TimeoutError" after "sec" if job is not completed
    try:
        async with asyncio.timeout(2):
            await greet_me()
    except TimeoutError as e:
        print(f"Timeout error happened: {e}")

    print(await without_awaiting_task)

    # 👉 Running the task into ".to_thread" function, that run on block task into different thread
    print("⌛ RUNNING BLOCKING TASKS")
    results = await asyncio.gather(
        asyncio.to_thread(block_task, "job1", 2),
        asyncio.to_thread(block_task, "job2", 2),
    )
    print(f"Results: {results}")


if __name__ == "__main__":
    # 👉 Starts the event loop, unlike "node.js" where event loop automatically started
    asyncio.run(main())
