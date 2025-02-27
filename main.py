from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter 

## lets create an instance of a GraphQLRouter 
graphql_router = GraphQLRouter(..., path="/", graphql_ide="lolo-sandbox")

app = FastAPI()

app.include_router(graphql_router)

