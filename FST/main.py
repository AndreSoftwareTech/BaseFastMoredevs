from fastapi import FastAPI 
from fastapi import HTTPException, status
from models import Aluno
from fastapi import Response
from fastapi import Path


app = FastAPI()

@app.get('/')
async def raiz():
    return { "mensagem": "Seja bem vindo ao more devs" }

alunos = {
    1: {
        "nome": "Andre",
        "idade": "25",
        "email": "andre@andre"
    },
    2: {
        "nome": "vitor",
        "idade": "25",
        "email": "vitor@vitor"
    }
}

@app.get('/alunos')
async def get_alunos(): 
    return alunos
@app.get('/alunos/{aluno_id}')
async def get_aluno(aluno_id: int = Path(default=None, title='ID Aluno', description='deve ser entre 1 ou 2', gt=0, lt=3)): 
    try:
        aluno = alunos[aluno_id]
        return aluno

    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado'
        )

@app.post('/alunos', status_code=status.HTTP_201_CREATED)
async def post_aluno(aluno: Aluno):
    next_id : int = len(alunos) +1
    alunos[next_id] = aluno
    del aluno.id
    return aluno

@app.get('/calculadora')
async def calcular(a, b, c): 
    soma = a + b + c

@app.put('/alunos/{aluno_id}')
async def put_aluno(aluno_id: int, aluno: Aluno):
    
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno nao encontrado com este id {aluno_id}')


@app.delete('/alunos/{aluno_id}')
async def delete_aluno(aluno_id: int):
    
    if aluno_id in alunos:
        del alunos[aluno_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno nao encontrado com este id {aluno_id}')




if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host= "127.0.0.1",
        port=8000,
        log_level = "info",
        reload = True
    )