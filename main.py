import asyncio
import time

async def createPdf(i):
    time.sleep(2) # The PDF writer, like this statement will block until complete
    print("hello", i)

async def main():
    tasks = []
    for i in range(10):
       tasks.append(asyncio.create_task(createPdf(i)))
    await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())