import strawberry
import strawberry.experimental.pydantic as strawberry_pydantic

from models.contracts import EntityContract


@strawberry_pydantic.interface(model=EntityContract,
                               description='Describes a abstraget entity with a ID')
class Entity:
  id: strawberry.auto