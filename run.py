import strawberry

from src.mutation import Mutation
from src.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
