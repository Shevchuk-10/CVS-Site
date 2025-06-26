from fastapi import APIRouter, Form, HTTPException
from typing import List
from datetime import datetime
from models import Post

router = APIRouter()
posts: List[Post] = []
post_id_counter = 1

@router.get("/api/posts", response_model=List[Post])
def get_all_posts():
    return posts

@router.post("/api/posts", response_model=Post)
def create_post(title: str = Form(...), content: str = Form(...), author: str = Form(...)):
    global post_id_counter
    post = Post(
        id=post_id_counter,
        title=title,
        content=content,
        author=author,
        created_at=datetime.now()
    )
    posts.append(post)
    post_id_counter += 1
    return post

@router.delete("/api/posts/{post_id}")
def delete_post(post_id: int):
    global posts
    for post in posts:
        if post.id == post_id:
            posts.remove(post)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Post not found")

