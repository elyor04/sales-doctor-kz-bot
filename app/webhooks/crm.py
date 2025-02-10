from fastapi import APIRouter, Request, Response, HTTPException
from app.helpers import extractLeadIds, makeLeadMessage
from app.bot import bot
from app.config import CRM_WEBHOOK, CHAT_ID

router = APIRouter()


@router.post(f"/{CRM_WEBHOOK}")
async def crm_webhook(request: Request):
    try:
        data = await request.form()
    except:
        raise HTTPException(status_code=400, detail="Invalid Form")

    parsedData = {key: data[key] for key in data}
    leadIds = extractLeadIds(parsedData)

    for leadId in leadIds:
        leadMessage = await makeLeadMessage(leadId)
        await bot.send_message(chat_id=CHAT_ID, text=leadMessage)

    return Response(status_code=200)
