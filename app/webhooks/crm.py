from fastapi import APIRouter, Request, Response
from app.helpers import extractLeadIds, makeLeadMessage
from app.bot import bot
from app.config import CRM_WEBHOOK, CHAT_ID

router = APIRouter()


@router.post(CRM_WEBHOOK)
async def crm_webhook(request: Request):
    formData = await request.form()
    parsedData = {key: formData[key] for key in formData}

    leadIds = extractLeadIds(parsedData)
    for leadId in leadIds:
        leadMessage = await makeLeadMessage(leadId)
        await bot.send_message(chat_id=CHAT_ID, text=leadMessage)

    return Response(status_code=200)
