from fastapi import FastAPI
from . import bot, crm


def register_webhooks(app: FastAPI):
    app.include_router(bot.router)
    app.include_router(crm.router)
