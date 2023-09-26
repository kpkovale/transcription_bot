import aioschedule
import asyncio
from utils.token_generator import IAMToken


async def scheduler():
    aioschedule.every().minutes(60).do(refresh_token)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(60)


async def refresh_token():
    tokenizer = IAMToken()
    token = tokenizer.iam_token
