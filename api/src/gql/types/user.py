import strawberry
import strawberry.experimental.pydantic as strawberry_pydantic

from gql.interfaces import Entity
from models.contracts import UserContract


@strawberry_pydantic.type(model=UserContract,
                          description='Represent data of a registered user')
class User(Entity):
  name: strawberry.auto
  email: strawberry.auto