import logging
import uvicorn
from app.webhooks import register_webhooks
from app.handlers import register_handlers
from app.app import app
from app.bot import dp
from app.config import HOST, PORT

register_webhooks(app)
register_handlers(dp)

if __name__ == "__main__":
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    uvicorn.run(app, host=HOST, port=PORT)
