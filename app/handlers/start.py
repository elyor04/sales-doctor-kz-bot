from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ChatType

router = Router()


@router.message(Command("start"), F.chat.type == ChatType.PRIVATE)
async def start_handler(message: Message):
    await message.answer(f"👋 Здравствуйте, <b>{message.from_user.full_name}</b>!")
