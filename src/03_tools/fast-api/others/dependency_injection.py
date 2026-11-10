"""
🟡 Dependency injection is a way to inject something, like methods or classes, inside another function.
🟡 There might be a route that needs something again and again. Instead of creating the same thing again, we just create it once
   and inject it as a dependency using a dependent function.
"""

from fastapi import Depends, Header, HTTPException, Query


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
