import strawberry


@strawberry.type
class Query:
  @strawberry.field
  def users(self) -> list[str]:
    return []


schema = strawberry.Schema(query=Query)