from app.utils import crmClient


async def getCompanyById(id: int):
    response = await crmClient.get(f"api/v4/companies/{id}")

    if response.status == 200:
        return await response.json()

    return None
