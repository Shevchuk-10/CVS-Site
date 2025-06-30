from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.responses import HTMLResponse, RedirectResponse
from database import add_post, delete_post, get_all_posts
router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@router.post("/api/posts/add")
def create_post(
    request: Request,
    id: int = Form(...),
    title: str = Form(...),
    img: str = Form(...),
    content: str = Form(...),
    author: str = Form(...),
    created_at: str = Form(...)
):
    post_data = {
        "id": id,
        "title": title,
        "img": img,
        "content": content,
        "author": author,
        "created_at": created_at
    }
    add_post(post_data)
    return RedirectResponse("/dashboard", status_code=302)
    #return templates.TemplateResponse('dashboard.html', {'request': request})

@router.delete("/api/posts/delete")
def remove_post(id: int):
    success = delete_post(id)
    if success:
        return {"message": "Пост успешно удален"}
    return {"message": "Пост не найден"}

@router.get("/api/posts")
def list_posts():
    return get_all_posts()

@router.get("/posts/create", response_class=HTMLResponse)
def get_create_post_form(request: Request):
    return templates.TemplateResponse("posts/add_post.html", {"request": request})

@router.get("/posts/delete", response_class=HTMLResponse)
def get_delete_post_form(request: Request):
    return templates.TemplateResponse("posts/delete_post.html", {"request": request})

@router.post("/api/posts/delete")
def delete_post_form(post_id: int = Form(...)):
    success = delete_post(post_id)
    if success:
        return {"message": f"Пост с ID {post_id} успешно удалён"}
    return {"message": f"Пост с ID {post_id} не найден"}