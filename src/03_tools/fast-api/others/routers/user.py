from fastapi import APIRouter, Depends

from ..dependency_injection import get_admin, pagination

router = APIRouter(prefix="/users", tags=["users"], dependencies=[Depends(get_admin)])


@router.get("")
def get_users(p: dict = Depends(pagination)):  # noqa: B008
    return p
