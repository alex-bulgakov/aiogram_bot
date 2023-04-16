import asyncio


async def send_time(sec: int) -> None:
    while True:
        await asyncio.sleep(sec)
        print(f'Прошло {sec} секунд')

# print(send_time(2), send_time(5), sep='\n')

async def main() -> None:
    t1 = asyncio.create_task(send_time(2))
    t2 = asyncio.create_task(send_time(5))

    await t1
    await t2

if __name__ == '__main__':
    asyncio.run(main())