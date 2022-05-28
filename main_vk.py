import logging
from vkbottle.bot import Bot, Message

from main import *

bot = Bot("1e0f79485bec796c92ef5953271337d3e17f0e4558f4e1bafd3d42c5dc976fae266c101271e29990ddd6a")

logging.basicConfig(level=logging.INFO)

@bot.on.message(text="/расписание")
async def eat_handler(message: Message):
    await message.answer(NewLessons())

bot.run_forever()