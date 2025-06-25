from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def read_root(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request, 'dima': 'dima.html', 'andrew': 'andrew.html'}
    )


@app.get('/andrew', name='andrew')
def andrew_html(request: Request):
    return templates.TemplateResponse(
        name='andrew.html',
        context={'request': request}
    )


@app.get('/dima', name='dima')
def dima_html():
    return templates.TemplateResponse(
        name='dima.html'
    )
