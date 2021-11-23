import strawberry


@strawberry.interface(description='Describes a abstract entity with a ID')
class Entity:
  id: strawberry.ID