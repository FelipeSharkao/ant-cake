import strawberry

from fastapi import FastAPI
from gql import schema
from repos.mongo import setup as setup_mongo
from strawberry.fastapi import GraphQLRouter


class MongoRouter(GraphQLRouter):
  async def execute(self, *args, **kwargs):
    await setup_mongo()
    return await super().execute(*args, **kwargs)


app = FastAPI()
app.include_router(MongoRouter(schema), prefix='/graphql')