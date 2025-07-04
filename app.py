from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from config import username, password
from database import init_db
from token_manager import create_token, verify_token
from fastapi.middleware.cors import CORSMiddleware
from routers import posts, auth
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError



app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return templates.TemplateResponse(
        "404.html",
        {
            "request": request,
            "code_error": exc.status_code,
            "message": exc.detail if exc.detail else "Щось пішло не так"
        },
        status_code=exc.status_code
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return templates.TemplateResponse(
        "404.html",
        {
            "request": request,
            "code_error": 422,
            "message": "Помилка валідації"
        },
        status_code=422
    )

@app.get("/dashboard")
async def dashboard(request: Request):
    token = request.cookies.get("auth_token")
    user = verify_token(token) if token else None

    if not user:
        return RedirectResponse("/admin", status_code=303)

    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/logout")
def logout():
    response = RedirectResponse("/", status_code=302)
    response.delete_cookie("auth_token")
    return response


app.include_router(posts.router)
app.include_router(auth.router)



