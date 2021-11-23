import strawberry

from .types import User
from repos.mongo import UserRepository


@strawberry.type
class Query:
  @strawberry.field
  async def users(self) -> list[User]:
    return await UserRepository.head()


schema = strawberry.Schema(query=Query)