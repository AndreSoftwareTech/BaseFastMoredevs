from fastapi import FastAPI 
from fastapi import HTTPException, status


app = FastAPI()

@app.get('/')
async def raiz():
    return { "mensagem": "Seja bem vindo ao more devs" }

alunos = {
    1: "Lirinha",
    2: "Vander boladao",
    3: "Dieter",
    4: "William"
}

@app.get('/alunos')
async def get_alunos(): 
    return alunos

@app.get('/alunos/{aluno_id}')
async def get_aluno(aluno_id: int): 
    aluno = alunos[aluno_id]
    alunos.update({'id': aluno_id})

    return aluno
       


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host= "127.0.0.1",
        port=8000,
        log_level = "info",
        reload = True
    )