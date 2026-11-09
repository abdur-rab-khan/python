from fastapi import APIRouter, Depends

from ..dependency_injection import pagination

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_users(p: dict = Depends(pagination)):  # noqa: B008
    return p
