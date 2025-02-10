from app.utils import crmClient


async def getUserById(id: int):
    response = await crmClient.get(f"api/v4/users/{id}")

    if response.status == 200:
        return await response.json()

    return None
