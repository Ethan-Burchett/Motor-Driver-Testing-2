import asyncio

async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)   # what does the await keyword do? 
    print("Coroutine finished")

async def main():
    print("Main started")
    await my_coroutine()
    print("Main finished")

asyncio.run(main())