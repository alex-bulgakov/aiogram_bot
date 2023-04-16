import asyncio


async def print_1_second() -> None:
    n = 0
    while True:
        await asyncio.sleep(1)
        print(f'{n}  second' if n % 3 != 0 else '')
        n += 1


async def print_3_second() -> None:
    n = 0
    while True:
        await asyncio.sleep(3)
        print('3 seconds')
        n += 1


async def main():
    task1 = asyncio.create_task(print_1_second())
    task2 = asyncio.create_task(print_3_second())

    await task1
    await task2


asyncio.run(main())
