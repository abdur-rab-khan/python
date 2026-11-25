"""
🟡 A router is like a mini application for a particular endpoint. Instead of adding everything in a
   single main.py file, we split based on endpoint, like users, accounts, etc.
🟡 To Create a router. We need an API router from FastAPI, and we can provide a prefix. In main.py, we
   just have to include it using `app.include_router(user.router, prefix="/user")`, can be written here.
🟡 Need to note that FastAPI isn't a singleton by default, so if you add a class as a dependency, it
   will create a new instance for each request. To update this behavior to a singleton, we need to use a method that will use an LRU cache, and from that function, we will return that class instance.
🟡 We can Add a list of dependencies which are needed for only this particular route inside the API
   router.
"""

from fastapi import APIRouter, Depends

from ..dependency_injection import get_admin, pagination

router = APIRouter(prefix="/users", tags=["users"], dependencies=[Depends(get_admin)])


@router.get("")
def get_users(p: dict = Depends(pagination)):  # noqa: B008
    return p
