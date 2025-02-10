from app.utils import crmClient


async def getLeadById(id: int):
    response = await crmClient.get(
        f"api/v4/leads/{id}",
        params={"with": "contacts"},
    )

    if response.status == 200:
        return await response.json()

    return None
