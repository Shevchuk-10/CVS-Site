from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from config import username, password

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
def dima_html(request: Request):
    return templates.TemplateResponse(
        name='dima.html',
        context={'request': request}
    )


@app.post("/login")
def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == username and password == password:
        return RedirectResponse("/dashboard", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Неверный логин или пароль"})


@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/admin")
def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
