"""
🟡 Dependency injection is a way to inject something, like methods or classes, inside another function.
🟡 There might be a route that needs something again and again. Instead of creating the same thing again, we just create it once
   and inject it as a dependency using a dependent function.
"""

from fastapi import Depends, Header, HTTPException
from pydantic import Field


# 🟡 Now we can pass the pagination function using dependency injection.
def pagination(page: int = 1, limit: int = Field(default=10, le=10, ge=100)):
    return {"page": page, "limit": limit}


# 🟡 Let's use dependency injection into another dependency injection.
def get_current_user(token: str = Header()):
    return {"id": 1, "name": "Python"}


def get_admin(user=Depends(get_current_user)):  # noqa: B008
    if user["name"] != "Python":
        raise HTTPException(status_code=403, detail="Not allowed")
    return user
