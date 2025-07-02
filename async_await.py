import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("World!")

async def main():
    await say_hello()


asyncio.run(main())  # Run the event loop
