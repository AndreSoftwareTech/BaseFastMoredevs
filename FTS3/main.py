from fastapi import FastAPI
from routes import router_aluno
from routes import router_usuario

app = FastAPI()


app.include_router(router_aluno.router, tags=['alunos'])
app.include_router(router_usuario.router, tags=['usuario'])

if __name__ == 'main':
    import uvicorn
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
        log_level="info",
        reload=True
    )