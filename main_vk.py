import logging
from vkbottle.bot import Bot, Message

from main import *

from config import TOKEN

bot = Bot(TOKEN)

logging.basicConfig(level=logging.INFO)

@bot.on.message(text="/расписание")
async def eat_handler(message: Message):
    await message.answer(NewLessons())

bot.run_forever()