from aiohttp import ClientSession
from app.config import CRM_BASE_URL, CRM_TOKEN


class AmoCrmClient:
    def __init__(self):
        self.session: ClientSession = None

    async def initialize(self):
        self.session = ClientSession(base_url=CRM_BASE_URL)

    async def request(self, method: str, url: str, **kwargs):
        if not self.session:
            raise RuntimeError("AmoCrmClient session not initialized, call 'initialize' first.")

        if "headers" not in kwargs:
            kwargs["headers"] = {}

        kwargs["headers"]["Authorization"] = f"Bearer {CRM_TOKEN}"
        return await self.session.request(method, url, **kwargs)

    async def get(self, url: str, **kwargs):
        return await self.request("GET", url, **kwargs)

    async def close(self):
        if self.session:
            await self.session.close()


crmClient = AmoCrmClient()
