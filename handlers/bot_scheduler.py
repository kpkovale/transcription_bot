import aioschedule
import asyncio


async def scheduler():
    aioschedule.every().day.at("15:00").do(remind)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(50)


async def remind():
    print("Hi!")
