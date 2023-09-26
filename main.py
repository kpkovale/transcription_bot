import asyncio
from telebot.async_telebot import AsyncTeleBot

from bot_config import *
from utils.bot_logger import logger
from handlers.bot_scheduler import scheduler

from telebot import apihelper

apihelper.ENABLE_MIDDLEWARE = True

# States storage
from telebot.asyncio_storage import StateMemoryStorage

# middlewares
from middlewares.antiflood_middleware import AntiSpamMiddleware

# filters
from filters import bind_custom_filters

state_storage = StateMemoryStorage()
# I recommend increasing num_threads
bot = AsyncTeleBot(TOKEN, parse_mode='markdown')

# Middlewares
bot.setup_middleware(AntiSpamMiddleware(2, bot))

from handlers import register_custom_handlers


async def main():
    await asyncio.gather(bot.delete_my_commands(),
                         bot.infinity_polling(skip_pending=True, logger_level=LOG_LEVEL)#,
                         #scheduler()
                         )

if __name__ == '__main__':
    logger.log(LOG_LEVEL, "Clearing bot commands")

    # register filters
    bind_custom_filters(bot)
    # register bot handlers
    register_custom_handlers(bot)

    logger.log(LOG_LEVEL, "Starting bot")
    asyncio.run(main())
    # bot.infinity_polling()
