#pip install fastapi uvicorn jinja2
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI("API de Alunos")
#config o diretorio dos templates jinja2
templates = Jinja2Templates(directory="templates")


#Pasta static para servir os arquivos (CSS, Imagens ou JV)
app.mount("/static", StaticFiles(directory="static", name="static"))

alunos = [
    {"nome": "Felipe", "nota": 8.5},
    {"nome": "Laura", "nota": 9.0},
    {"nome": "Yasmin", "nota": 8.0}
]


#Rota Inicial
@app.get("/", response_class=HTMLResponse)
def exibir_alunos(request: Request):
    return templates.TemplateResponse(
        "aluno.html", {"request": request, "Lista_alunos": alunos}
    )