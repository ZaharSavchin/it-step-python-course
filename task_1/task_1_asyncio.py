from time import time
import asyncio


async def factorial(n):
    if n == 0:
        return 1
    else:
        return n * await factorial(n-1)


async def main():
    start = time()
    for i in range(100000):
        await factorial(800)
    print(time() - start)


if __name__ == '__main__':
    asyncio.run(main())


