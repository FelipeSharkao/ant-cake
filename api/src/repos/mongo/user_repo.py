from beanie import Document
from models.contracts import UserContract

class UserDocument(Document, UserContract):
  password: str


class UserRepository:
  @staticmethod
  async def head(limit: int=10) -> list[UserDocument]:
    return await UserDocument.find_all().limit(limit).to_list()