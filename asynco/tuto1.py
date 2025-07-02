import asyncio

async def main():
    print(await asyncio.sleep(2, result='hello'))

async def anotherOne():
    print(await asyncio.sleep(1,result="new Hello"))

if __name__ == "__main__":
    asyncio.run(main(),debug=True)