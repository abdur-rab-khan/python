from typing import Annotated, Literal

from fastapi import Cookie, FastAPI, HTTPException, Path, Query, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field


# 👉 Model for making response in a structured manner using ""pydantic"" and generic in python
class APIResponse[T = None](BaseModel):
    status_code: Annotated[int, Field(default=200, ge=200, le=599)]
    message: Annotated[str, Field(min_length=10, max_length=255)]
    data: T | None = None

    @computed_field
    def success(self) -> bool:
        return 200 <= self.status_code < 300

    @computed_field
    def status(self) -> Literal["success", "failed"]:
        return "success" if 200 <= self.status_code < 300 else "failed"


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


# <------------------------------------------> ERROR HANDLING <------------------------------------------>
# 👉 In FastAPI to throw an error we simple raise an exception via "HTTPException", FastAPI automatically handles that but to make sure everything is structured.
# 👉 We use ""exception_handler"" where we can override the default exception handlers, by providing the exception that we want to override like the ""exception_handler"" decorator
@app.exception_handler(RequestValidationError)
async def handle_request_validation_error(_, exc: RequestValidationError):

    error_details = []
    for error in exc.errors():
        # e.g, "body -> age: input should be valid number"
        location = " -> ".join(loc for loc in error["loc"])
        error_details.append(f"{location}: {error['msg']}")

    error_message = "Validation Failed: " + "; ".join(error_details)

    # Force to strict to match APIResponse schema validation
    response_body = APIResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, message=error_message
    )

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content=response_body.model_dump(exclude={"data"}),
    )


@app.exception_handler(HTTPException)
async def handle_http_exception(_, exc: HTTPException):
    response_body = APIResponse(status_code=exc.status_code, message=str(exc.detail))
    return JSONResponse(
        status_code=exc.status_code, content=response_body.model_dump(exclude={"data"})
    )


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
) -> APIResponse[dict]:
    return APIResponse[dict](
        status_code=200,
        data={"item_id": item_id},
        message=f"here's the item with this {item_id}",
    )


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
# 👉 In FastAPI we can get ""cookies"" and ""headers"" same way like we define ""Body()"", ""Query()"", where we directly infer to inject stuff that we want using ""Annotated""
# 👉 We can also make ""pydantic"" model to group and declare validation on cookies
@app.get("/cookies")
async def get_cookies(cookie: Annotated[str, Cookie()]):
    return {"cookie": cookie}
