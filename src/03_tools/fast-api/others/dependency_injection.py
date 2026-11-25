"""
🟡 Dependency injection is a way to inject something, like methods or classes, inside another function.
🟡 Suppose we do a service to a route. Instead of creating the same logic again for each route, we
   create it once and provide it as a dependency.
🟡 Unlike NestJS's singleton pattern, here in FastAPI, for each request, the dependency instance will
   be created. To prevent this, we need to use LRU cache, and from that method, we need to return that class.
"""

from fastapi import Depends, HTTPException, Query


# 🟡 Now we can pass the pagination function using dependency injection.
def pagination(
    page: int = Query(1, description="Current page"),
    limit: int = Query(10, ge=10, le=100, description="Number of items needed"),
):
    return {"page": page, "limit": limit}


# 🟡 Let's use dependency injection into another dependency injection.
# def get_current_user(token: str = Header()): --> Here we might we token from the header
def get_current_user():
    return {"id": 1, "name": "Python"}


# 🟡 In real application we might have authentication logic that we add using dependency injection to our private routes
def get_admin(user=Depends(get_current_user)):  # noqa: B008
    if user["name"] != "Python":
        raise HTTPException(status_code=403, detail="Not allowed")
    return user
