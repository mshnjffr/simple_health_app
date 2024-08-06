from fastapi import APIRouter
import uuid

myuuid = uuid.uuid4()
router = APIRouter()

@router.get("/secure", status_code=200)
async def secure():
    return {f"secureSecret": {myuuid}}