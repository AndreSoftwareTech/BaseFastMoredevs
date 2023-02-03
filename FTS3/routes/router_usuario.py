from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/usuario')
async def get_usuario():
    return {'Testa usuario'}