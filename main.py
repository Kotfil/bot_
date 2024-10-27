from fastapi import FastAPI
import asyncio
from telethon import TelegramClient, events
import env

app = FastAPI()

bot = TelegramClient('bot', env.API_ID, env.API_HASH)

@app.on_event("startup")
async def startup_event():
    # Запускаем бота при запуске FastAPI
    await bot.start(bot_token=env.API_TOKEN)

    @bot.on(events.NewMessage(pattern="/start"))
    async def start(event):
        await event.respond('Привет! Бот работает.')
        print('Получен запрос /start')

    # Запуск клиента в асинхронном цикле
    asyncio.create_task(bot.run_until_disconnected())

@app.get("/")
async def root():
    return {"message": "FastAPI приложение запущено"}

# Запуск FastAPI с помощью uvicorn:
# uvicorn main:app --reload
