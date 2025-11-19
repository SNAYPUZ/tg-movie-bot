from aiogram import Bot, Dispatcher, types
import asyncio, os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    @dp.message()
    async def echo(msg: types.Message):
        await msg.answer("Bot ishladi! ZIP namunaviy loyiha yuklandi.")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
