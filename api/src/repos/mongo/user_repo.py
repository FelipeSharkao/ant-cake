from beanie import Document


class UserDocument(Document):
  name: str
  email: str
  password: str


class UserRepository:
  @staticmethod
  async def head(limit: int=10) -> list[UserDocument]:
    return await UserDocument.find_all().limit(limit).to_list()