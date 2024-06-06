import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from src.mutation import Mutation
from src.query import Query
from src.subscription import Subscription

schema = strawberry.Schema(query=Query,
                           mutation=Mutation,
                           subscription=Subscription)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
