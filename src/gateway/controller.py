from fastapi import APIRouter, Request

gateway_router = APIRouter(
    prefix='/gateway',
    tags=['gateway']
)

@gateway_router.get("/")
async def getRoot():
    return "AI-Gateway validator API"