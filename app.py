from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from config import username, password
from token_manager import create_token, verify_token
from fastapi.middleware.cors import CORSMiddleware
from routers import posts, auth

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Заміни на фронтовий домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', name='index')
def read_root(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request, 'dima': 'dima.html', 'andrew': 'andrew.html'}
    )


@app.get('/andrew', name='andrew')
def andrew_html(request: Request):
    return templates.TemplateResponse("andrew.html", {"request": request})


@app.get('/dima', name='dima')
def dima_html(request: Request):
    return templates.TemplateResponse("dima.html", {"request": request})

@app.get('/404', name='404')
def not_found(request: Request):
    return templates.TemplateResponse("404.html", {"request": request, "code_error": "404"})

@app.get("/admin")
def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def login_post(request: Request, login_username: str = Form(...), login_password: str = Form(...)):
    if login_username == username and login_password == password:
        token = create_token(login_username)
        response = RedirectResponse("/dashboard", status_code=302)
        response.set_cookie("auth_token", token, httponly=True)
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error": "Неверный логин или пароль"})


@app.get("/dashboard")
def dashboard(request: Request):
    token = request.cookies.get("auth_token")
    user = verify_token(token) if token else None

    if not user:
        return RedirectResponse("/admin", status_code=302)

    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})


@app.get("/logout")
def logout():
    response = RedirectResponse("/", status_code=302)
    response.delete_cookie("auth_token")
    return response


app.include_router(posts.router)
app.include_router(auth.router)
