from .user_repo import UserDocument, UserRepository
from beanie import init_beanie
from env import Mongo
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

__all__ = ['setup', 'UserRepository']


client: Optional[AsyncIOMotorClient] = None

async def setup() -> None:
  global client
  if client is None:
    client = AsyncIOMotorClient(Mongo.URI)
    await init_beanie(database=client[Mongo.DB_NAME], document_models=[UserDocument])
