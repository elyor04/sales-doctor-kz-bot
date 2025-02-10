from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.bot import bot
from app.utils import crmClient
from app.config import DOMAIN_NAME, BOT_WEBHOOK


@asynccontextmanager
async def lifespan(app: FastAPI):
    await crmClient.initialize()
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(DOMAIN_NAME + BOT_WEBHOOK)

    yield

    await bot.delete_webhook()
    await bot.session.close()
    await crmClient.close()


app = FastAPI(lifespan=lifespan)
