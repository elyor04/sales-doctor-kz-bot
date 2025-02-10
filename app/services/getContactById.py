from app.utils import crmClient


async def getContactById(id: int):
    response = await crmClient.get(f"api/v4/contacts/{id}")

    if response.status == 200:
        return await response.json()

    return None
