import asyncio


async def send_hello() -> None:
    await asyncio.sleep(1)
    print('hello')


async def send_bye() -> None:
    await asyncio.sleep(2)
    print('Bye')


async def main():
    await send_hello()
    await send_bye()


asyncio.run(main())