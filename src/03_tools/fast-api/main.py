from typing import Annotated, Any, Literal

from fastapi import Cookie, FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    price: float
    tax: float | None = None
    description: str | None = None


class FilterParams(BaseModel):
    limit: Annotated[int, Field(default=100, gt=0, le=100)]
    offset: Annotated[int, Field(default=0, ge=0)]
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "Python"}


# <------------------------------------------> PATH PARAMS <------------------------------------------>
# 👉 FastAPI can automatically infer the ""path params"" by just using the ""params name"" (e.g "item_id"), and automatically validate/parse based on type and send error to the client, under the hood it uses ""pydantic"" for this.
# 👉 In FastAPI we can directly apply validation logic to each ""path params"" using ""Path"" function via ""Annotated"" and also using ""Query"" for query.
@app.get("/items/{item_id}")
async def get_items(
    item_id: Annotated[
        int, Path(title="Id of the item that you want to get", gt=1, le=1000)
    ],
):
    return {"item_id": item_id}


# <------------------------------------------> QUERY PARAMS <------------------------------------------>
# 👉 FastAPI automatically infer parameters other than """PATH PARAMS""" as query and same as ""PATH PARAMS"" here as well validate/parse happens and send error to the client.
# 👉 We can also perform validation on the ""query params"" that we are getting by adding into the ""Annotated[type, Query(default="", max_length=2, ...etc)]""
# 👉 If we have related ""Query Params"", we can make a ""Pydantic"" model and group all the related ""Queries"" and define using ""Query()""
@app.put("/items", status_code=201)
async def put_items(
    item_id: str,
    item: list[str],
    # q: Annotated[str | None, Query(max_length=10)] = None,
    filter_query: Annotated[FilterParams, Query()],
):
    return {
        "item_id": item_id,
        "item": item,
        "query": filter_query.model_dump() if filter_query else None,
    }


# <------------------------------------------> REQUEST BODY <------------------------------------------>
# 👉 FastAPI automatically infer as ""Request Body"" if the type is ""dict, list and pydantic"" or if you want to make ""string, number etc"" body you have to provide annotation with body like this """body: Annotated[type, Body()]"""
# 👉 Since it's using pydantic, FastAPI will automatically sanitize/validate/parse the incoming data based on the ""Pydantic Schema""
# 👉 We provide multiple ""body"" and FastAPI will automatically infer them as a group "body" dict, like we can have "item: Item, user: User" and then fastapi we expect to give data like this "{'item': item, 'user': user}"
@app.post("/items")
async def create_item(item: Item):
    return item.model_dump(exclude={"price"})


# <------------------------------------------> COOKIES <------------------------------------------>
# 👉 In FastAPI we can get ""cookies"" and ""headers"" same way like we define ""Body()"", ""Query()"" to infer to the ""query and body"".
# 👉 We can also make ""pydantic"" model to group and declare validation on cookies
@app.get("/cookies")
async def get_cookies(cookie: Annotated[str, Cookie()]):
    return {"cookie": cookie}
