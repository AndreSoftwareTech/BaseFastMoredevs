from fastapi import APIRouter

router = APIRouter()


@router.get('/api/v1/alunos')
async def get_alunos():
    return {'Testa Aluno'}