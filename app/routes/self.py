from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/self", status_code=200)
async def self(request: Request):
    headers = {key: value for key, value in request.headers.items()}
    return headers
