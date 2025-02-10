from fastapi import APIRouter, Request, Response, HTTPException
from aiogram.types import Update
from app.bot import bot, dp
from app.config import BOT_WEBHOOK

router = APIRouter()


@router.post(f"/{BOT_WEBHOOK}")
async def bot_webhook(request: Request):
    try:
        data = await request.json()
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    update = Update(**data)
    await dp.feed_update(bot, update)

    return Response(status_code=200)
